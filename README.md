# Курсова робота у КАІ з дисципліни ООП на мові програмування Python
```
├── BLL
│   ├── entity_services.py
│   └── __init__.py
├── classes_CourseWork.png
├── classes_CourseWork.puml
├── DAL
│   ├── abstract_filemanager.py
│   ├── Entities
│   │   ├── football_match.py
│   │   ├── football_player.py
│   │   ├── football_stadium.py
│   │   └── __init__.py
│   ├── file_manipulations.py
│   └── __init__.py
├── __init__.py
├── main.py
├── packages_CourseWork.png
├── packages_CourseWork.puml
├── PL
│   ├── __init__.py
│   └── menu_service.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_football_match.py
    ├── test_football_player.py
    └── test_football_stadium.py
```

# Project Overview

Small course project implementing OOP concepts in Python. Contains layers:
- DAL — data access and entity definitions
- BLL — business logic services
- PL  — presentation (CLI) menu
- tests — pytest unit tests

# Requirements

- Python 3.11 or newer
- pip
- Linux (instructions use Linux commands) or windows

Dependencies are pinned in requirements.txt.

# Installation
1. Install python to your PC via:
    - [official website](https://www.python.org/downloads/)
    - Or packets in linux ```sudo apt install python<version>```

2. Create and activate a virtual environment:
   - python -m venv .venv
   - source .venv/bin/activate or .venv/Scripts/activate

3. Upgrade pip and install dependencies:
   - pip install --upgrade pip
   - pip install -r requirements.txt

# Running the application

From project root:
- python3 main.py

Interrupt (Ctrl+C) handling prompts to confirm exit.

# Tests

Run unit tests with pytest:
- cd into tests
- pytest .

# Test coverage

Install coverage (already in requirements.txt). Generate coverage report:
- coverage run -m pytest
- coverage report
- coverage html
- xdg-open htmlcov/index.html

# Notes

- Add project-specific environment variables in a .env file if needed.
- __pycache__ and other build artifacts should be ignored via .gitignore.

# Sources (consulted)
- Python — https://www.python.org/
- pytest documentation — https://docs.pytest.org
- Diagram generation - https://pypi.org/project/pylint/
- coverage.py documentation — https://coverage.readthedocs.io/