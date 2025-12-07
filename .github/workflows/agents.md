# AI-Assisted Development Documentation

## 1. AI Tools Used
* **Google Gemini** (Primary AI assistant, used to generate code and analyze project progress)
* **GitHub Copilot** (Assisted in code development)

## 2. Usage Strategy
I utilized AI as a "Senior Developer" pair programmer to guide me through the development lifecycle. My usage focused on three key areas:

* **Architecture & Standards:** Ensuring my project structure (`src` vs `tests`, `.gitignore`) met professional standards and rubric requirements.
* **Code Generation & Refactoring:** Converting concepts into working Python code, specifically for the `Player` class logic and implementing the `rich` library for UI.
* **Debugging & Environment:** Resolving pathing issues with Python modules (`ModuleNotFoundError`) and configuring the `pytest` environment.

## 3. Specific Examples of Prompts

**Prompt 1: Project Structuring & Validation**
> "You are a Senior SWE who specializes in CLI applications... analyze my"

* **Outcome:** The AI analyzed my rubric and file list, immediately identifying that I was missing a `.gitignore` file and helping me organize my `src/` and `tests/` directories to maximize points for "Professional Code Organization."

**Prompt 2: Debugging Module Errors**
> "ModuleNotFoundError: No module named 'src'"

* **Outcome:** I encountered a blocking error when trying to run my code. The AI explained that because I was using a `src` directory, I needed to run the script as a module (`python -m src.main`) rather than a file path. This taught me a new concept regarding Python's package execution.

**Prompt 3: Feature Implementation**
> "Make the CLI more UI focused by using the rich library package"

* **Outcome:** The AI provided a complete refactor of my `main.py` to utilize the `Rich` library, replacing standard print statements with colored tables and formatted headers. This directly addressed the "Professional CLI Application" rubric requirement.

## 4. Reflection on AI Impact
AI assistance significantly accelerated the setup phase of this project. Instead of spending hours reading documentation on how to set up `argparse` or configure `pytest`, I was able to get a working skeleton in minutes. This allowed me to focus my time on the actual logic—how fantasy points are calculated and how the data is modeled.

It also acted as a quality assurance check. By pasting my file structure, the AI was able to point out missing files (like `.gitignore`) that I would have otherwise overlooked, preventing potential point deductions.

## 5. Challenges and Limitations
One specific challenge was context management. At one point, the AI assumed I was using a standard Linux environment when I was using Git Bash on Windows, leading to minor command confusion (e.g., `tree` command vs `find`). I had to explicitly clarify my environment ("I'm using Git Bash") to get the correct commands. This reinforced that AI tools require precise context to be effective.