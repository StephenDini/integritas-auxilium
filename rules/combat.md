# Combat Reference

## Combat Sequence Per Round
1. **Declare** spells and melee movement (spells and movement must be declared before initiative)
2. **Initiative**: Each side rolls 1d6; highest acts first. Ties = simultaneous or re-roll.
3. Winning side acts: monster morale → movement → missile attacks → spell casting → melee attacks
4. Other sides act in initiative order.

## Initiative
- **Standard**: Each *side* rolls 1d6. Highest wins.
- **Individual (optional)**: Each combatant rolls 1d6, modified by DEX bonus.
- **Slow weapons**: Two-handed melee weapons always act *last*, regardless of initiative.

| DEX | AC Mod | Missile | Initiative |
|-----|--------|---------|------------|
| 3 | –3 | –3 | –2 |
| 4–5 | –2 | –2 | –1 |
| 6–8 | –1 | –1 | –1 |
| 9–12 | — | — | — |
| 13–15 | +1 | +1 | +1 |
| 16–17 | +2 | +2 | +1 |
| 18 | +3 | +3 | +2 |

## Attack Rolls (Descending AC)
1. Roll 1d20
2. Apply modifiers (STR for melee; DEX + range for missile)
3. Look up result on attack matrix for attacker's THAC0 row → find which AC is hit
4. If hit AC ≤ opponent's AC, the attack hits

**Shortcut**: Roll needed = THAC0 − target's AC (e.g., THAC0 17 vs AC 4 → need 13+)

**Ascending AC (optional)**: Roll 1d20 + attack bonus; if result ≥ opponent's AAC, hit.

| Attack Roll | Natural 1 | Natural 20 |
|-------------|-----------|------------|
| Always miss | Always hit |

## Attack Matrix (Key Rows)
| THAC0 | [Bonus] | Hit AC: –3 | 0 | 2 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---------|-----------|---|---|---|---|---|---|---|---|
| 19 | [0] | 20 | 19 | 17 | 15 | 14 | 13 | 12 | 11 | 10 |
| 18 | [+1] | 20 | 18 | 16 | 14 | 13 | 12 | 11 | 10 | 9 |
| 17 | [+2] | 20 | 17 | 15 | 13 | 12 | 11 | 10 | 9 | 8 |
| 16 | [+3] | 19 | 16 | 14 | 12 | 11 | 10 | 9 | 8 | 7 |
| 15 | [+4] | 18 | 15 | 13 | 11 | 10 | 9 | 8 | 7 | 6 |
| 14 | [+5] | 17 | 14 | 12 | 10 | 9 | 8 | 7 | 6 | 5 |
| 13 | [+6] | 16 | 13 | 11 | 9 | 8 | 7 | 6 | 5 | 4 |
| 12 | [+7] | 15 | 12 | 10 | 8 | 7 | 6 | 5 | 4 | 3 |

## Armour Class Reference
| Armour | AC (desc) | AC (asc) |
|--------|-----------|----------|
| Unarmoured | 9 | [10] |
| Leather | 7 | [12] |
| Chainmail | 5 | [14] |
| Plate mail | 3 | [16] |
| + Shield | –1 | +1 |

## Damage
- **Default**: All weapons deal 1d6.
- **Variable (optional)**: Use weapon-specific damage dice (see equipment).
- STR modifier applies to melee damage.
- Minimum 1 damage on a hit, even after penalties.

## Movement in Combat
- **Encounter movement**: 1/3 of base movement rate per round.
- **Fighting withdrawal**: Move backward up to half encounter rate; requires clear path.
- **Retreat**: Full encounter rate; cannot attack; opponent gets +2 to hit and ignores shield AC bonus this round.
- **Running**: Base movement rate in feet per round. After 30 rounds: –2 to attacks, damage, and AC.

## Missile Attacks
| Range | Modifier |
|-------|----------|
| Short | +1 to hit |
| Medium | None |
| Long | –1 to hit |
| Beyond long | Cannot attack |

- Possible when opponents are more than 5' apart.
- Cover: –1 to –4 to hit (partial); impossible (full).

## Spell Casting in Combat
- Must declare before initiative.
- Cannot move and cast in same round.
- Must be able to speak and move hands.
- If hit or fails a save *before* acting after losing initiative: spell is disrupted and lost.
- Spells must have line of sight to target.

## Morale (Optional)
- Monsters roll 2d6 vs morale rating.
- If roll **exceeds** morale: surrender or flee.
- If roll **≤** morale: continue fighting.
- Check on: first death in group, when half the group is incapacitated.
- Two successful morale checks = fight to the death.

| Troop Type | Morale |
|------------|--------|
| Untrained militia | 6 |
| Barbarian horde | 7 |
| Trained warriors | 8 |
| Mounted | +1 |
| Elite troops | +1 |
| Fanatics/berserkers | +2 |

## Special Attacks

### Backstab (Thief)
- Attack from behind against unaware opponent.
- **+4 to hit**, **×2 damage**.
- At level 6: ×2 damage multiplier.

### Turning Undead (Cleric)
- Roll 2d6; compare to Turning Table vs HD of undead.
- Success: roll 2d6 to determine total HD affected (turned or destroyed).
- Turned undead flee and will not contact the cleric.
- Destroyed (D): instantly annihilated.
- At least 1 undead always affected on a success.
- Mixed groups: lowest HD affected first.

*See cleric.md for full turning table.*

### Paralysed/Helpless Opponents
- Automatically hit in melee; only roll damage.

### Charging
- Require clear 20-yard run; double damage on hit (lance or appropriate weapon).

### Subduing (Optional)
- Announce intent; use blunt weapons only.
- Track subdual damage separately.
- At 0 HP from subdual: surrender.

## Death and Healing
- **Death**: Reduced to 0 HP or less.
- **Destruction of items**: If killed by lightning bolt, breath weapon, etc., gear may be destroyed.
- **Natural healing**: 1d3 HP per full day of complete rest. Interrupted rest = no healing.
- **Magical healing**: Instant; stacks with natural healing.
- **Resting in dungeon**: 1 turn (10 min) rest required per hour or suffer –1 to attack and damage.
- **Resting overland**: 1 full day per 6 days of travel or suffer –1 to hit and damage.

## Surprise
- Roll 1d6 for each side not expecting encounter.
- **1 or 2**: That side is surprised.
- Surprised side loses its action for one round; other side gains a free round.
- Carrying light in darkness: usually cannot surprise opponents.
