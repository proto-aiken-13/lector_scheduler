from scheduling.input_reader import read_lector_availability
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
