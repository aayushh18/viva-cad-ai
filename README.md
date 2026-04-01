# FREE CAD AI PRO

An enterprise-grade AI-powered CAD generation platform.

## Project Structure

- `backend/`
  - `main.py`: FastAPI server handling design lifecycle and API requests.
  - `models.py`: SQLModel database schema for designs and iterations.
  - `AIPromptEngine.py`: Integration with OpenAI (GPT-4o) for generating Structured JSON Mechanical Schema (SJMS).
  - `FreeCADAdapter.py`: Logic to convert SJMS into FreeCAD Python scripts with visualization fixes and manifold exports.
  - `requirements.txt`: Python dependencies.
  - `.env`: Environment variables (API keys, FreeCAD path).
- `frontend/`
  - `src/App.tsx`: React frontend with history view, prompt input, and execution logs.
  - `src/index.css`: Professional glassmorphic dark-mode styles.
  - `package.json`: Frontend dependencies and Electron configuration.
- `run.py`: Orchestration script to launch both backend and frontend services.

## Prerequisites

- **FreeCAD**: Must be installed on your system.
- **Python 3.10+**
- **Node.js & npm**
- **OpenAI API Key**

## Setup & Execution

1. **Configure Environment**:
   - Create a `.env` file in the `backend/` folder based on `.env.example`.
   - Set your `OPENAI_API_KEY`.
   - Ensure `FREECAD_PATH` points to your `freecadcmd` executable.

2. **Install Dependencies**:
   - Backend: `pip install -r backend/requirements.txt`
   - Frontend: `npm install` inside the `frontend/` folder.

3. **Run the Application (via Terminal)**:
   - Open your terminal.
   - Navigate to the project root directory:
     ```bash
     cd /path/to/viva-cad-ai
     ```
   - Run the orchestration script:
     ```bash
     python3 run.py
     ```
   - This will start both the backend FastAPI server and the frontend development server automatically.

## Usage

- Enter a prompt to generate CAD models. Example commands:
  - `"Create a box with length 120, width 80, and height 10"`
  - `"Create a plate 120x80 with 4 holes"`
  - `"Make a cylinder with radius 15 and height 50"`
  - `"Create a 100x100x100 box with a 10mm fillet on the top edges"`
- View the generated **SJMS Schema**.
- Click **Build in FreeCAD** to generate the model and see visualization in your FreeCAD GUI (if running).
- Check the **Execution Logs** for logs and file paths of generated `.FCStd` and `.STEP` files.
