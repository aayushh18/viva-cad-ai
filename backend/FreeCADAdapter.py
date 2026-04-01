import os
import sys
import subprocess

sys.path.append('/usr/lib/freecad/lib')

class FreeCADAdapter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_script(self, schema: dict, output_base: str) -> str:
        """Converts AI JSON to a Python script using the Rule Engine."""
        from CommandGenerator import CommandGenerator
        from FreeCADRuleEngine import build_model, generate_script as rule_generate_script
        
        # 1. Generate text commands from schema
        print("STEP 1: JSON received")
        commands = CommandGenerator.generate(schema)
        print("STEP 2: Commands generated", commands)
        
        # 2. Build model dictionary from text commands
        model = build_model(commands)
        print("STEP 3: Model built", model)
        
        # 3. Output paths
        fcstd_path = os.path.abspath(f"{output_base}.FCStd").replace("\\", "/")
        
        # 4. Generate the actual python script using the rule engine
        script_code = rule_generate_script(model, fcstd_path)
        
        return script_code

    def execute_script(self, script_path: str, headless: bool = True) -> dict:
        """Executes the script using FreeCAD."""
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        env_path = os.getenv("FREECAD_PATH")
        
        # Dynamically resolve binary path depending on headless mode
        if headless:
            if env_path and env_path.endswith("freecad"):
                bin_cmd = env_path + "cmd"
            elif env_path and "freecadcmd" in env_path:
                bin_cmd = env_path
            else:
                bin_cmd = "freecadcmd"
        else:
            if env_path:
                bin_cmd = env_path.replace("freecadcmd", "freecad")
            else:
                bin_cmd = "freecad"
                
        cmd = [bin_cmd, script_path]
            
        try:
            if not headless:
                # Run FreeCAD in GUI mode and wait until it's closed to capture the result
                result = subprocess.run(cmd, capture_output=True, text=True)
            else:
                # Increased timeout to 120 seconds for demonstration builds
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0 and "freecadcmd" in cmd[0] and "FreeCAD" not in result.stderr:
                # Some Linux FreeCAD installs don't have freecadcmd mapped if they are appimages/snaps
                # Let's fallback if an error occurred in pure execution.
                pass
            
            if result.returncode != 0:
                return {"success": False, "error": result.stderr or result.stdout}
            
            if "SCRIPT_ERROR" in result.stdout and "SCRIPT_ERROR: None" not in result.stdout:
                # Check actual trace
                err_lines = [l for l in result.stdout.split() if "SCRIPT_ERROR" in l and "None" not in l]
                if err_lines:
                    return {"success": False, "error": result.stdout}
                
            return {"success": True, "log": result.stdout}
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "FreeCAD execution timed out (120s limit)."}
        except Exception as e:
            return {"success": False, "error": f"Failed to run FreeCAD: {str(e)}"}
