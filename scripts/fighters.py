import pandas as pd

fighters_df = pd.read_csv('./csv/all_fighters.csv')
fighters_options =  dict(zip(fighters_df['N_Name'], fighters_df['id']))

def get_fighter_stats(figherId):
    stats = fighters_df[fighters_df['id']==figherId]
    return stats.iloc[0]