# Notes

A lightweight task management application built with **Python** and **NiceGUI**.

The application provides a simple notepad-like interface where each task can be assigned an **Effort Level**. Tasks can be marked complete, sorted by effort, and are automatically saved locally.

---

## Features

- Add tasks
- Delete tasks
- Mark tasks as completed
- Effort Levels
  - ⭐ Very Low
  - ⭐⭐ Low
  - ⭐⭐⭐ Medium
  - ⭐⭐⭐⭐ High
  - ⭐⭐⭐⭐⭐ Very High
- Sort tasks
  - High → Low
  - Low → High
- Automatic local persistence using `tasks.json`
- Cross-platform development
- Windows executable built automatically using GitHub Actions

---

# Tech Stack

- Python 3.13
- NiceGUI
- uv (Package Manager)
- PyInstaller
- GitHub Actions

---

# Project Structure

```
notes/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── pages/
│   │   └── home.py
│   ├── services/
│   └── main.py
│
├── .github/
│   └── workflows/
│
├── pyproject.toml
├── uv.lock
├── tasks.json
└── README.md
```

---

# Prerequisites

Install:

- Python 3.13+
- uv
- Git

Install uv:

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

---

# Clone the Repository

```bash
git clone https://github.com/Sisir2311/notes-app.git

cd notes-app
```

---

# Install Dependencies

Run:

```bash
uv sync
```

This command:

- Creates the virtual environment (if needed)
- Installs all project dependencies
- Uses versions locked in `uv.lock`

---

# Running the Application

Run the application as a module:

```bash
uv run python -m app.main
```

The application will start on:

```
http://127.0.0.1:8080
```

Your browser should open automatically.

---

# Development Workflow

Whenever you make changes:

Run:

```bash
uv run python -m app.main
```

Stop the application with:

```
Ctrl + C
```

---

# Local Storage

Tasks are automatically stored inside:

```
tasks.json
```

This file is created automatically the first time you add a task.

Example:

```json
[
    {
        "text": "Finish README",
        "effort": 4,
        "completed": false
    }
]
```

---

# Building a Windows Executable

The project uses **GitHub Actions** to automatically generate a Windows executable.

Every push to the `main` branch triggers the workflow.

Workflow:

```
Push Code
      │
      ▼
GitHub Actions
      │
      ▼
Windows Runner
      │
      ▼
PyInstaller
      │
      ▼
Notes.exe
```

The executable can be downloaded from:

```
GitHub

↓

Actions

↓

Latest Successful Workflow

↓

Artifacts

↓

Notes-Windows.zip
```

---

# Useful Commands

Install dependencies

```bash
uv sync
```

Run the application

```bash
uv run python -m app.main
```

Add a package

```bash
uv add <package-name>
```

Update dependencies

```bash
uv sync --upgrade
```

Show installed packages

```bash
uv pip list
```

---

# Git Workflow

Check status

```bash
git status
```

Stage changes

```bash
git add .
```

Commit

```bash
git commit -m "Your commit message"
```

Push

```bash
git push origin main
```

---

# Future Enhancements

- User Authentication
- Cloud Synchronization
- SQLite Database
- Priority Dashboard
- Search
- Categories
- Tags
- Desktop Packaging
- Dark Mode
- Export / Import
- Notes + Checklist Support

---

# Author

**Sisir Goljana**

GitHub:
https://github.com/Sisir2311