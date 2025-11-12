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

# Example usage
## Football player
<img width="1425" height="91" alt="image" src="https://github.com/user-attachments/assets/cf381d62-509b-4aef-afec-9c7a3b6f225d" />
Adding a player with these charestistics, as result see .json file with them:
<img width="628" height="373" alt="image" src="https://github.com/user-attachments/assets/d1252f74-aeb8-49d6-8918-23f41593408d" />

## Football match
<img width="1587" height="135" alt="image" src="https://github.com/user-attachments/assets/1c2676e2-5351-4564-948e-9b6841a8b9f6" />
<img width="1092" height="139" alt="image" src="https://github.com/user-attachments/assets/f415af80-1538-4202-90ca-fd8d4691a8d6" />
Adding the match and previous player to the match, and out result is:
<img width="668" height="734" alt="image" src="https://github.com/user-attachments/assets/d40f48ee-7b95-4c6b-8387-8e87494a38bf" />

## Football stadium
<img width="965" height="47" alt="image" src="https://github.com/user-attachments/assets/e7bb1de5-00bf-4190-ac4f-e37af01687cf" />
<img width="372" height="73" alt="image" src="https://github.com/user-attachments/assets/e959edce-5ced-4571-853d-d4426ca8c51f" />

Creating stadium and adding a previously made match here, result:
<img width="608" height="767" alt="image" src="https://github.com/user-attachments/assets/eb706b44-cbc3-42fb-a063-6174a9fe6810" />


