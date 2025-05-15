import os

# Define the folder and file structure
base_dir = "backend"
scheduling_dir = os.path.join(base_dir, "scheduling")

files_to_create = {
    os.path.join(scheduling_dir, "__init__.py"): "",

    os.path.join(scheduling_dir, "input_reader.py"): '''import pandas as pd

def read_lector_availability(filepath):
    df = pd.read_excel(filepath)
    lector_data = []

    for _, row in df.iterrows():
        name = row['Name']
        unavailable = row['Unavailable Dates']
        unavailable_dates = []

        if pd.notna(unavailable):
            unavailable_dates = [d.strip() for d in str(unavailable).split(',')]

        lector_data.append({
            'name': name,
            'unavailable': unavailable_dates
        })

    return lector_data
''',

    os.path.join(scheduling_dir, "scheduler.py"): '''def assign_lectors(lector_data, dates):
    schedule = []

    for i, date in enumerate(dates):
        for lector in lector_data:
            if date not in lector['unavailable']:
                schedule.append({
                    'Date': date,
                    'Lector': lector['name']
                })
                break  # Assign one lector per date
    return schedule
''',

    os.path.join(scheduling_dir, "output_writer.py"): '''import pandas as pd

def write_schedule(schedule, filepath):
    df = pd.DataFrame(schedule)
    df.to_excel(filepath, index=False)
''',

    os.path.join(base_dir, "run_scheduler.py"): '''from scheduling.input_reader import read_lector_availability
from scheduling.scheduler import assign_lectors
from scheduling.output_writer import write_schedule

# Define schedule dates (for demo)
schedule_dates = [
    '2024-06-01',
    '2024-06-08',
    '2024-06-15',
    '2024-06-22',
    '2024-06-29',
]

lector_data = read_lector_availability("lector_availability.xlsx")
schedule = assign_lectors(lector_data, schedule_dates)
write_schedule(schedule, "generated_lector_schedule.xlsx")

print("Schedule created: generated_lector_schedule.xlsx")
'''
}

# Create directories and write files
for path, content in files_to_create.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Backend scheduler structure has been set up in the 'backend/' directory.")
