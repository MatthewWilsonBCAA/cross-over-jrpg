tiles = ["basic_tile"]
backgrounds = ["backgrounds/dark_stone"]

import json

with open("world_one.json") as f:
    data = json.load(f)
test_arena = []
base_x = data.pop(0)
y = data.pop(0)
for i in data:
    x = base_x
    for j in i:
        raw = int(j)
        if raw > 0:
            test_arena.append(((x, y), tiles[raw - 1], True))
        else:
            raw *= -1
            # print("RAW", raw)
            test_arena.append(((x, y), backgrounds[raw - 1], False))
        x += 75
    y += 75
