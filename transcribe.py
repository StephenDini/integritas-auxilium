import sys
import os
import subprocess
import tempfile
from openai import OpenAI

CHUNK_MINUTES = 10

def split_audio(input_path, tmp_dir):
    chunk_pattern = os.path.join(tmp_dir, "chunk_%03d.mp3")
    cmd = [
        "ffmpeg", "-i", input_path,
        "-f", "segment",
        "-segment_time", str(CHUNK_MINUTES * 60),
        "-ac", "1",
        "-ar", "16000",
        "-b:a", "32k",
        chunk_pattern,
        "-y", "-loglevel", "error"
    ]
    subprocess.run(cmd, check=True)
    chunks = sorted([
        os.path.join(tmp_dir, f)
        for f in os.listdir(tmp_dir)
        if f.startswith("chunk_") and f.endswith(".mp3")
    ])
    return chunks

def transcribe(audio_path):
    client = OpenAI()

    print(f"Splitting audio into {CHUNK_MINUTES}-minute chunks...")
    with tempfile.TemporaryDirectory() as tmp_dir:
        chunks = split_audio(audio_path, tmp_dir)
        print(f"  {len(chunks)} chunks created")

        base = os.path.splitext(os.path.basename(audio_path))[0]
        out_path = os.path.join(os.path.dirname(audio_path), f"{base}-transcript.txt")

        with open(out_path, "w", encoding="utf-8") as out:
            for i, chunk_path in enumerate(chunks):
                offset_seconds = i * CHUNK_MINUTES * 60
                print(f"  Transcribing chunk {i+1}/{len(chunks)} (offset {offset_seconds//60}m)...")

                with open(chunk_path, "rb") as f:
                    result = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=f,
                        response_format="verbose_json",
                        timestamp_granularities=["segment"]
                    )

                for segment in result.segments:
                    start = offset_seconds + segment.start
                    end = offset_seconds + segment.end
                    h_s, m_s, s_s = int(start//3600), int((start%3600)//60), start%60
                    h_e, m_e, s_e = int(end//3600), int((end%3600)//60), end%60
                    timestamp = f"[{h_s:02d}:{m_s:02d}:{s_s:05.2f} --> {h_e:02d}:{m_e:02d}:{s_e:05.2f}]"
                    line = f"{timestamp}  {segment.text.strip()}"
                    print(line)
                    out.write(line + "\n")

    print(f"\nTranscript saved: {out_path}")
    return out_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file>")
        sys.exit(1)

    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    transcribe(sys.argv[1])
