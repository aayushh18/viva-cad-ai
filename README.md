# VivaCAD-AI

### Intelligent Text-to-CAD Automation Engine using NLP, FreeCAD & FastAPI

VivaCAD-AI is an advanced AI-assisted CAD automation framework designed to transform natural language engineering prompts into parametric 3D CAD models.

Developed during an industry research internship at the Bhabha Atomic Research Centre (BARC) in collaboration with Parul University, the system combines Natural Language Processing (NLP), deterministic geometric scripting, and CAD kernel automation to streamline mechanical design workflows.

The primary objective of this project is to reduce repetitive manual drafting efforts by enabling intelligent generation of CAD geometries directly from textual design specifications.

---

## Core Features

### ➢  Natural Language Driven CAD Generation
Transforms human-readable engineering prompts into executable CAD operations.

### ➢  Parametric 3D Modeling
Generates dimensionally accurate and editable parametric CAD geometries.

### ➢  FreeCAD Python Automation
Utilizes the FreeCAD Python API for automated model synthesis and geometry processing.

### ➢  Full-Stack Architecture
Integrated frontend-backend ecosystem using React, FastAPI, and REST APIs.

### ➢  Dockerized Deployment
Supports reproducible and isolated deployment environments using Docker containers.

### ➢  Hybrid AI + Rule-Based Validation
Combines NLP interpretation with deterministic scripting logic to improve geometric reliability and reduce invalid model generation.

### ➢  X11 GUI Forwarding Support
Supports FreeCAD GUI rendering inside Docker containers using X11 forwarding for Linux-based environments.

---

# ➢ System Architecture

```text
   Natural Language Prompt
            │
            ▼
   NLP Interpretation Layer
            │
            ▼
 Structured Design Parameters
            │
            ▼
 CAD Logic Generation Engine
            │
            ▼
FreeCAD Python Scripting Layer
            │
            ▼
Parametric 3D CAD Output* for logs and file paths of generated `.FCStd` and `.STEP` files.

```
<img width="1000" height="400" alt="0" src="https://github.com/user-attachments/assets/093556c8-2903-43ab-974e-db6e6b6a0333" />

<img width="1000" height="400" alt="2" src="https://github.com/user-attachments/assets/9d0c6873-39e4-45b1-b886-480ff163fbcb" />

<img width="1000" height="400" alt="3" src="https://github.com/user-attachments/assets/b143ee17-acd7-4b49-b0c9-a1494c45bad6" />

<img width="1000" height="400" alt="4" src="https://github.com/user-attachments/assets/1d74c7ff-e661-4a04-a39d-ec46a7d27196" />


## ➢ Tech Stack
- Python
- FastAPI
- React.js
- FreeCAD API
- Docker
- MongoDB
- HuggingFace Transformers

## ➢ Research Background
Developed during an industry internship at Bhabha Atomic Research Centre (BARC), Mumbai under the Nuclear Recycle Group (NRG), Government of India.

