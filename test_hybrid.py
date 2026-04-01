import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from backend.CommandGenerator import CommandGenerator
from backend.FreeCADRuleEngine import build_model, generate_script

def test():
    schema = {
        "base": {
            "type": "plate",
            "length": 100,
            "width": 80,
            "thickness": 10
        },
        "features": [
            {
                "type": "hole",
                "radius": 5,
                "count": 4,
                "pattern": "corner"
            },
            {
                "type": "fillet",
                "radius": 3
            }
        ]
    }
    
    print("1. Original AI JSON Schema:")
    print(json.dumps(schema, indent=2))
    
    # Generate commands
    commands = CommandGenerator.generate(schema)
    print("\n2. Generated Commands:")
    for c in commands:
        print(f"  - {c}")
        
    # Build model
    model = build_model(commands)
    print("\n3. Built Model Operations:")
    print(json.dumps(model, indent=2))
    
    # Generate Script
    script = generate_script(model, "/tmp/test.FCStd")
    print("\n4. Generated FreeCAD Script (preview):")
    print('\n'.join(script.splitlines()[:15]))
    print("...")
    print("TEST SUCCESS")
    
if __name__ == "__main__":
    test()
