from backend.CommandGenerator import CommandGenerator
import json

schema = {
    "type": "flange",
    "standard": "DN50"
}

commands = CommandGenerator.generate(schema)
print("Generated Commands for DN50:")
for cmd in commands:
    print(f" - {cmd}")

schema2 = {
    "type": "flange",
    "standard": "UNKNOWN"
}

commands2 = CommandGenerator.generate(schema2)
print("\nGenerated Commands for Unknown Standard:")
for cmd in commands2:
    print(f" - {cmd}")
