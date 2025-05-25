import pandas as pd
import joblib
import numpy as np
import os

fighters_df = pd.read_csv('./csv/all_fighters.csv')
all_fights_ufc = pd.read_csv('./csv/df_all_fights.csv')
current_directory = os.path.dirname(__file__)
root_directory = os.path.abspath(os.path.join(current_directory, '..'))
model_path = os.path.join(root_directory, 'model.pkl')

def get_weight_classes():
    classes = all_fights_ufc['weight_class'].unique()
    return classes

def get_methods():
    methods = all_fights_ufc['method'].unique()
    return methods

def get_fighter_options(w_class):
    f = fighters_df[fighters_df['weight_class']== w_class]
    fighters_options = dict(zip(f['N_Name'], f['id']))
    return fighters_options

def get_fighter_stats(figherId):
    stats = fighters_df[fighters_df['id']==figherId]
    return stats.iloc[0]

def get_fighter_info(figtherId):
    fighter_w = all_fights_ufc[all_fights_ufc['winner_id']==figtherId]
    fighter_l = all_fights_ufc[all_fights_ufc['loser_id']==figtherId]
    fighter_ww = fighter_w[['winner_significant_strike_percentage','winner_total_strike_percentage','winner_knockdowns','winner_takedown_percentage','winner_takedowns','winner_submission_attempts']]
    fighter_ll = fighter_l[['loser_significant_strike_percentage','loser_total_strike_percentage','loser_knockdowns','loser_takedown_percentage','loser_takedowns','loser_submission_attempts']]
    fighter_ww = fighter_ww.rename(columns={
        'winner_significant_strike_percentage': 'strike_accuracy' ,
        'winner_total_strike_percentage': 'total_strike_accuracy',
        'winner_knockdowns': 'knockdowns',
        'winner_takedown_percentage': 'takedown_accuracy',
        'winner_takedowns': 'takedowns',
        'winner_submission_attempts': 'submission_attempts'})

    fighter_ll = fighter_ll.rename(columns={
        'loser_significant_strike_percentage': 'strike_accuracy',
        'loser_total_strike_percentage': 'total_strike_accuracy',
        'loser_knockdowns': 'knockdowns',
        'loser_takedown_percentage': 'takedown_accuracy',
        'loser_takedowns': 'takedowns',
        'loser_submission_attempts': 'submission_attempts'})
    all_fights_wl = pd.concat([fighter_ww,fighter_ll], sort=False)
    means = all_fights_wl.mean()
    return means

def get_fight_prediction(fighter1Id, fighter2Id, weight_class):
    model = joblib.load(model_path)
    fighter1_info = get_fighter_info(fighter1Id)
    fighter2_info = get_fighter_info(fighter2Id)
    fight_stats = {
        'strike_accuracy_diff': fighter1_info['strike_accuracy'] - fighter2_info['strike_accuracy'],
        'total_strike_accuracy_diff': fighter1_info['total_strike_accuracy'] - fighter2_info['total_strike_accuracy'],
        'knockdowns_diff': fighter1_info['knockdowns'] - fighter2_info['knockdowns'],
        'takedown_accuracy_diff': fighter1_info['takedown_accuracy'] - fighter2_info['takedown_accuracy'],
        'takedowns_diff': fighter1_info['takedowns'] - fighter2_info['takedowns'],
        'submission_attempts_diff': fighter1_info['submission_attempts'] - fighter2_info['submission_attempts'],
        'weight_class': weight_class
    }
    methods = get_methods()
    fights_to_predict = []
    for m in methods:
        new_fight = fight_stats
        new_fight['method'] = m
        fights_to_predict.append(new_fight)

    x = pd.DataFrame(fights_to_predict)
    prediction = model.predict(x)

    f1_counts = (prediction == 0).sum()
    f2_counts = (prediction == 1).sum()

    winner = ''
    if f1_counts > f2_counts:
        winner = get_fighter_stats(fighter1Id)['N_Name']
    else:
        winner = get_fighter_stats(fighter2Id)['N_Name']

    return winner






