def assign_lectors(lector_data, dates):
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
