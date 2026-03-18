"""
Discord channel scraper — ADHDnD Gaming Group / #ttrpgs

Instructions:
1. Run script
2. Log into Discord in the browser
3. Navigate to ADHDnD Gaming Group > #ttrpgs
4. In Discord, press Ctrl+Home to jump to oldest messages
5. Wait until you see "Beginning of #ttrpgs" at the top
6. Press ENTER in this terminal
"""

import re
import time
import json
import urllib.request
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

ARCHIVE_DIR = Path(__file__).parent
IMAGE_DIR = ARCHIVE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

def sanitize(s):
    return re.sub(r'[<>:"/\\|?*\s]', '_', str(s))[:80]

def download_image(url, name):
    try:
        clean_url = url.split("?")[0]
        ext = clean_url.split(".")[-1].lower()
        if ext not in ("png", "jpg", "jpeg", "gif", "webp"):
            ext = "png"
        dest = IMAGE_DIR / f"{name}.{ext}"
        if not dest.exists():
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                dest.write_bytes(r.read())
        return f"images/{dest.name}"
    except Exception as e:
        return f"[failed: {e}]"

def find_scroller(page):
    """Return the Discord message scroller element."""
    selectors = [
        'ol[class*="scrollerInner"]',
        '[class*="messagesWrapper"] [class*="scroller"]',
        '[class*="chatContent"] ol',
        'ol[data-list-id]',
    ]
    for sel in selectors:
        try:
            el = page.locator(sel).first
            if el.count() and el.bounding_box():
                return el
        except:
            continue
    return None

def extract_visible(page, seen_ids):
    """Pull all currently rendered messages from the DOM."""
    new_msgs = []
    items = page.locator('[id^="chat-messages-"]').all()

    for item in items:
        try:
            msg_id = item.get_attribute("id") or ""
            if not msg_id or msg_id in seen_ids:
                continue

            author = ""
            author_el = item.locator('[class*="username"]').first
            if author_el.count():
                author = author_el.inner_text(timeout=200)

            timestamp = ""
            time_el = item.locator("time").first
            if time_el.count():
                timestamp = time_el.get_attribute("datetime") or ""

            content = ""
            for part in item.locator('[class*="messageContent"]').all():
                content += part.inner_text(timeout=200) + " "
            content = content.strip()

            # Images and attachments
            image_urls = []
            for img in item.locator('img[src*="discordapp"]').all():
                src = img.get_attribute("src") or ""
                if src and src not in image_urls:
                    image_urls.append(src)
            for a in item.locator('a[href*="cdn.discordapp"], a[href*="media.discordapp"]').all():
                href = a.get_attribute("href") or ""
                if href and href not in image_urls:
                    image_urls.append(href)

            saved_images = []
            for i, url in enumerate(image_urls):
                fname = sanitize(f"{msg_id}_{i}")
                saved_images.append(download_image(url, fname))

            seen_ids.add(msg_id)
            new_msgs.append({
                "id": msg_id,
                "author": author.strip(),
                "timestamp": timestamp,
                "content": content,
                "images": saved_images,
            })
        except:
            continue

    return new_msgs

def at_bottom(page):
    return page.evaluate("""
        () => {
            const candidates = [...document.querySelectorAll('ol, [class*="scroller"]')]
                .filter(el => el.scrollHeight > 500);
            for (const el of candidates) {
                return el.scrollTop + el.clientHeight >= el.scrollHeight - 100;
            }
            return false;
        }
    """)

def scroll_down(page, px=250):
    page.evaluate(f"""
        () => {{
            const candidates = [...document.querySelectorAll('ol, [class*="scroller"]')]
                .filter(el => el.scrollHeight > 500);
            for (const el of candidates) {{
                el.scrollTop += {px};
                return;
            }}
        }}
    """)

def scrape(page):
    seen_ids = set()
    all_messages = []
    stall = 0
    iteration = 0

    print("\nCollecting messages...\n")

    while True:
        iteration += 1
        new = extract_visible(page, seen_ids)
        all_messages.extend(new)

        if new:
            stall = 0
            print(f"  [{iteration}] +{len(new)} new  |  total: {len(all_messages)}", flush=True)
        else:
            stall += 1

        bottom = at_bottom(page)

        if bottom and stall >= 4:
            print("\nBottom of channel reached.")
            break

        if stall >= 10:
            print("\nNo new messages for 10 iterations — stopping.")
            break

        scroll_down(page, px=250)
        time.sleep(1.5)  # Wait for Discord to render newly loaded messages

    return all_messages

def save(messages):
    messages.sort(key=lambda m: (m.get("timestamp") or "", m.get("id") or ""))

    json_path = ARCHIVE_DIR / "raw_messages.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

    md_path = ARCHIVE_DIR / "ttrpgs-channel-full.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# ADHDnD Gaming Group — #ttrpgs\n\n")
        f.write(f"Archived: {datetime.now().isoformat()}\n\n---\n\n")
        current_date = ""
        for msg in messages:
            ts = msg.get("timestamp", "")
            date = ts[:10] if len(ts) >= 10 else "unknown"
            if date != current_date:
                f.write(f"\n## {date}\n\n")
                current_date = date
            author = msg.get("author") or "—"
            content = msg.get("content", "")
            images = msg.get("images", [])
            time_str = ts[11:19] if len(ts) >= 19 else ""
            f.write(f"**{author}** `{time_str}`\n")
            if content:
                f.write(f"{content}\n")
            for img in images:
                f.write(f"![img]({img})\n")
            f.write("\n")

    print(f"\nDone.")
    print(f"  Messages : {len(messages)}")
    print(f"  Markdown : {md_path}")
    print(f"  JSON     : {json_path}")
    print(f"  Images   : {len(list(IMAGE_DIR.iterdir()))} files")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()

        print("Opening Discord...")
        page.goto("https://discord.com/app")
        time.sleep(3)

        print("\n" + "="*60)
        print("STEP 1: Log into Discord")
        print("STEP 2: Navigate to  ADHDnD Gaming Group > #ttrpgs")
        print("STEP 3: Press Ctrl+Home inside Discord to jump to the")
        print("        oldest messages")
        print("STEP 4: Wait until you see 'Beginning of #ttrpgs'")
        print("        at the top of the message list")
        print("STEP 5: Press ENTER here")
        print("="*60 + "\n")
        input("Press ENTER when you are at the TOP of #ttrpgs > ")

        time.sleep(1)
        messages = scrape(page)
        save(messages)
        browser.close()

if __name__ == "__main__":
    main()
