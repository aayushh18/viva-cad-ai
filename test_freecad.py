import os
from backend.FreeCADAdapter import FreeCADAdapter

schema = {
    "name": "Test_Part",
    "operations": [
        {
            "type": "box",
            "name": "base_box",
            "params": {"length": 20, "width": 20, "height": 10}
        },
        {
            "type": "cylinder",
            "name": "hole",
            "params": {"radius": 5, "height": 10}
        },
        {
            "type": "cut",
            "name": "final_part",
            "base": "base_box",
            "tool": "hole"
        }
    ]
}

adapter = FreeCADAdapter("./output")

print("Generating script...")
script_content = adapter.generate_script(schema, "./output/test_model")

with open("./output/test_script.py", "w") as f:
    f.write(script_content)

print("Executing script headless...")
result_headless = adapter.execute_script(os.path.abspath("./output/test_script.py"), headless=True)
print("Headless Result:", result_headless)

# For testing GUI mode without blocking forever in the automated test, we can just print what the command would be.
# print("Executing script GUI...")
# result_gui = adapter.execute_script(os.path.abspath("./output/test_script.py"), headless=False)
# print("GUI Result:", result_gui)
