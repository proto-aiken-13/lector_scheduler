import os
from pathlib import Path

def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n")

def main():
    base_dir = Path("lector-scheduler/backend")

    # Folder structure
    scheduler_dir = base_dir / "scheduler"
    app_dir = base_dir / "app"
    dirs = [
        scheduler_dir,
        app_dir / "api",
        app_dir / "models"
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # Files to create
    files = {
        scheduler_dir / "algorithm.py": '''\
import pandas as pd

def schedule_lectors(input_path, output_path):
    df = pd.read_excel(input_path)
    # TODO: Implement scheduling logic here
    df.to_excel(output_path, index=False)
''',

        scheduler_dir / "utils.py": '''\
def parse_availability(dataframe):
    # TODO: Parse availability info from DataFrame
    return []
''',

        base_dir / "run_scheduler.py": '''\
from scheduler.algorithm import schedule_lectors

if __name__ == "__main__":
    schedule_lectors("scheduler/input_sample.xlsx", "scheduler/output_example.xlsx")
''',

        base_dir / "requirements.txt": '''\
pandas
openpyxl
''',

        app_dir / "main.py": '''\
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API for Lector Scheduling"}
''',

        app_dir / "database.py": '''\
# Placeholder for future database connection logic
'''
    }

    for path, content in files.items():
        create_file(path, content)

    # Create a placeholder Excel file
    (scheduler_dir / "input_sample.xlsx").touch()

    print(f"✅ Backend project structure created at {base_dir.resolve()}")

if __name__ == "__main__":
    main()
