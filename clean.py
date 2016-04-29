import sys
import pandas as pd


def clean(file):
    df = pd.read_csv(file)

    map_to_number(df, 'action_type')
    map_to_number(df, 'combined_shot_type')
    map_to_number(df, 'season')
    map_to_number(df, 'shot_zone_area')
    map_to_number(df, 'shot_zone_basic')
    map_to_number(df, 'shot_zone_range')
    map_to_number(df, 'opponent')
    

    df['is_3pt'] = df.shot_type.map({'3PT Field Goal':1,'2PT Field Goal':0})

    game_rate(df)

    save_to_file(df)

def map_to_number(df, column_name):
    values =  {item: index for index, item in enumerate(df[column_name].unique())}
    df[column_name+'_number'] = df[column_name].map(values)

def save_to_file(df):
    file_name = file.replace('.csv', '')
    df.to_csv(file_name+'_cleaned.csv', index=False)
    df2 = df.loc[df.shot_made_flag.notnull()]
    df2.to_csv(file_name+'_cleaned_without_nulls.csv', index=False)
    df3 = df.loc[df.shot_made_flag.isnull()]
    df3.to_csv(file_name+'_cleaned_only_nulls.csv', index=False)

def game_rate(df):
    df['rate'] = pd.Series()
    df['points_game'] = pd.Series()
    df['points_attempt'] = pd.Series()
    grouped = df.groupby(df.game_id)
    for game,group in grouped:
        group_attempts = 0
        group_points = 0
        possible_points = 0
        for index,row in group.iterrows():
            if(group_attempts > 2):  #calibrar
                df.loc[df.shot_id == row.shot_id, 'rate'] =  group_points/possible_points
            else:
                df.loc[df.shot_id == row.shot_id, 'rate'] =  -1

            if(row.shot_made_flag == 1 or row.shot_made_flag == 0):
                if(row.is_3pt == 1):
                    possible_points += 3
                    if(row.shot_made_flag == 1):
                        group_points += 3
                else:
                    possible_points += 2
                    if(row.shot_made_flag == 1):
                        group_points += 2
                group_attempts += 1

            df.loc[df.shot_id == row.shot_id, 'points_game'] = group_points
            df.loc[df.shot_id == row.shot_id, 'points_attempt'] = possible_points

if __name__ == "__main__":
    file = sys.argv[1]
    clean(file)
