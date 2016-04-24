import sys
import pandas as pd


def clean(file):
    df = pd.read_csv(file)

    map_to_number(df, 'season')
    map_to_number(df, 'action_type')

    save_to_file(df)

def map_to_number(df, column_name):
    values =  {item: index for index, item in enumerate(df[column_name].unique())}
    df[column_name+'_number'] = df[column_name].map(values)

def save_to_file(df):
    file_name = file.replace('.csv', '')
    df.to_csv(file_name+'_cleaned.csv', index=False)
    df = df.loc[df.shot_made_flag.notnull()]
    df.to_csv(file_name+'_cleaned_without_nulls.csv', index=False)

if __name__ == "__main__":
    file = sys.argv[1]
    clean(file)
