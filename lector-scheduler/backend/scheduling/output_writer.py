import pandas as pd

def write_schedule(schedule, filepath):
    df = pd.DataFrame(schedule)
    df.to_excel(filepath, index=False)
