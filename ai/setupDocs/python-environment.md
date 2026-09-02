# Python Environment Setup

This guide explains how to create and configure the Python virtual environment for the AI module.

## 1. Navigate to the AI Directory

From the project root:

```powershell
cd ai
```

You should now be inside the `ai` directory.

## 2. Create the Virtual Environment

Create a virtual environment named `.venv`:

```powershell
python -m venv .venv
```

This creates the `.venv` directory inside `ai/`.

The `.venv` directory is ignored by Git and should not be committed.

## 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should show `(.venv)` at the beginning:

```text
(.venv) PS C:\...\Residential-Access-and-Visitor-Management-System\ai>
```

## 4. Install Project Dependencies

Make sure the virtual environment is activated, then run:

```powershell
pip install -r requirements.txt
```

This installs all Python packages required by the AI module.

## 5. Deactivate the Virtual Environment

When you are finished working with the AI module, deactivate the virtual environment:

```powershell
deactivate
```

The `(.venv)` prefix should disappear from the terminal.

## Quick Setup

For a fresh project clone:

```powershell
cd ai

python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

The Python environment is now ready.
