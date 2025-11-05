## Pandas Starter Project

A very basic project demonstrating reading a CSV with Pandas and performing simple operations.

### Setup

1. Create a virtual environment (optional but recommended)
   - Windows (PowerShell):
     ```bash
     python -m venv .venv
     .venv\\Scripts\\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run

```bash
python src/main.py
```

This will:
- Load `data/sample.csv`
- Print basic info and a grouped aggregation

### Project Structure

```
.
├─ data/
│  └─ sample.csv
├─ src/
│  └─ main.py
├─ .gitignore
├─ requirements.txt
└─ README.md
```


