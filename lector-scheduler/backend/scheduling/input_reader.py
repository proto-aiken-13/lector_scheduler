import pandas as pd

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
