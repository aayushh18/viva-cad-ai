import sys
import os
from backend.AIPromptEngine import AIPromptEngine

engine = AIPromptEngine()
print("Starting generation...")
try:
    res = engine.generate_schema("Create a box with length 10, width 10, height 5")
    print("Success! Generated Payload:")
    print(res["python_script"])
except Exception as e:
    print("Failed:")
    print(e)
