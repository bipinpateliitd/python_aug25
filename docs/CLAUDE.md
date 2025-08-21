# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python learning repository focused on basic programming concepts and GenAI integration. The codebase is organized into educational materials, practical exercises, and example applications.

## Architecture

### Core Structure
- **docs/**: Documentation and setup guides
  - **installation/**: Environment setup guides (Git, Miniconda, VS Code)
- **lessons/**: Structured learning modules organized by topic
  - **01_basics/**: Fundamental Python scripts
  - **02_variables_data_types/**: Variables and data types lessons
  - **03_operators/**: Python operators and expressions  
  - **04_strings/**: String manipulation and processing
  - **05_lists_tuples/**: Lists and tuples fundamentals
  - **06_data_structures_genai/**: Advanced data structures with GenAI applications
- **practice/**: Hands-on exercises and experiments
  - **basic_exercises/**: Simple Python practice scripts
  - **genai_experiments/**: AI integration experiments
- **tools/**: Utility scripts and AI-powered tools

### Key Components
- **tools/question_generator.py**: LangChain + Ollama (gemma3:270m) AI learning assistant
- **Lesson structure**: Each lesson contains theory notebooks and practical exercises
- **GenAI integration**: Progressive introduction of AI concepts throughout lessons

## Development Environment

### Python Environment
- **Python 3.12.9** (via Miniconda)
- No formal package manager configuration (requirements.txt, pyproject.toml)
- Dependencies managed manually: `langchain_ollama` for AI integration

### AI/ML Stack
- **Ollama**: Local LLM inference with gemma3:270m model (`/usr/local/bin/ollama`)
- **LangChain**: Framework for building AI applications
- Models are invoked using `ChatOllama` class for educational content generation

### Jupyter Environment
- **Jupyter**: Installed via Miniconda (`/home/bipin/miniconda3/bin/jupyter`)
- Primary development interface for lessons and experiments
- Notebooks combine code, markdown explanations, and practical exercises
- Standard Python kernel with educational focus

## Common Commands

### Running Python Scripts
```bash
python lessons/01_basics/hello_world.py           # Simple arithmetic demonstration
python tools/question_generator.py                # AI-powered learning assistant
python practice/basic_exercises/simple_tests.py   # Basic testing script
```

### Jupyter Notebooks
```bash
jupyter notebook               # Start Jupyter server for browser access
jupyter lab                    # Alternative modern interface
```

### Working with Lessons
```bash
# Navigate to specific lesson
cd lessons/02_variables_data_types
jupyter notebook lesson_02_variables_data_types.ipynb

# Run exercises
jupyter notebook exercises_02_variables_data_types.ipynb
```

### AI Model Usage
The tools/question_generator.py requires Ollama to be running locally with the gemma3:270m model installed:
```bash
ollama serve                   # Start Ollama service
ollama pull gemma3:270m        # Ensure model is available
```

### Dependencies Installation
Since no formal package management is used, install dependencies manually:
```bash
pip install langchain_ollama   # For AI integration
pip install jupyter            # For notebook environment
```

## Code Patterns

### String Processing
- Heavy use of string methods: `.strip()`, `.title()`, `.lower()`
- F-string formatting for dynamic content generation
- Input validation and cleaning patterns

### AI Integration
- Prompt engineering with context-aware templates
- Response processing and output formatting
- User input collection and sanitization

### Educational Structure
- Each lesson follows: Introduction → Examples → Exercises pattern
- Code examples are practical and immediately runnable
- Progressive complexity from basic syntax to AI applications