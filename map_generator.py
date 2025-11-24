import json
import random
import time

# Configuration
GRID_WIDTH = 20
GRID_HEIGHT = 15
# 0 = Grass, 1 = Rock (obstacle), 2 = Water
TERRAIN_TYPES = [0, 1, 2]

def generate_world():
    """Generates a random cozy garden map."""
    world_map = []
    
    for y in range(GRID_HEIGHT):
        row = []
        for x in range(GRID_WIDTH):
            # 80% Grass, 10% Rock, 10% Water
            tile = random.choices(TERRAIN_TYPES, weights=[80, 10, 10], k=1)[0]
            
            # Ensure starting area (0,0) is safe
            if x < 3 and y < 3:
                tile = 0
            
            row.append(tile)
        world_map.append(row)

    return world_map

def create_save_file():
    """Creates a JSON save file compatible with the JS game."""
    data = {
        "meta": {
            "version": "1.0",
            "timestamp": time.time(),
            "generator": "Python Tooling"
        },
        "player": {
            "x": 1,
            "y": 1,
            "seeds": 5,
            "water": 10
        },
        "world": {
            "width": GRID_WIDTH,
            "height": GRID_HEIGHT,
            "map": generate_world(),
            "plants": [] # Empty list for plants initially
        }
    }
    
    filename = "new_world_gen.txt"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Success! Generated '{filename}'. Import this file into the browser game.")

if __name__ == "__main__":
    create_save_file()
