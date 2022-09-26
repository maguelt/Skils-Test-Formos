import pandas as pd
import os

def daily_report():

    files = os.listdir(os.getcwd())

    csv_files = []

    for f in files:
        if f == 'sales.csv':
            csv_files.append(f)

    df = pd.concat((pd.read_csv(f)
                    for f in csv_files), ignore_index=True, sort=False)

    print(df.head())

daily_report()
