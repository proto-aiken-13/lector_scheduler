import pandas as pd

def schedule_lectors(input_path, output_path):
    df = pd.read_excel(input_path)
    # TODO: Implement scheduling logic here
    df.to_excel(output_path, index=False)
