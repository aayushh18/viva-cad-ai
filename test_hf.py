from backend.AIPromptEngine import AIPromptEngine
import json

def test():
    engine = AIPromptEngine()
    prompt = "create a box 100x100x10 and put a 5 radius hole in it then fillet the edges"
    print("Testing prompt:", prompt)
    
    response = engine.generate_schema(prompt)
    
    if isinstance(response, dict):
        print("\nParsed JSON Schema successfully:")
        print(json.dumps(response, indent=2))
        
        # Verify structure
        assert "name" in response
        assert "operations" in response
        assert isinstance(response["operations"], list)
        print("Structure check passed.")
    else:
        print(f"\nFailed! Returned string: {response}")

if __name__ == "__main__":
    test()
