#!/usr/bin/env python

'''
Author: ArkSealand
Date: 11.06.2021
Purpose: Valorant Battle Pass Calculator 
'''
from datetime import date, datetime, timedelta

'''
Steps:
1. Take into account user weeklies and dailies


2. Check if to include exp from weeklies and dailies so far. 


3. table of useful timeframes for spike /dm /unrated
''' 


# User fed inputs for calculations
response_dict = {}
response_dict['Tier'] = int(input('What number Tier are you currently on?'))
response_dict['Tier XP Progress'] = int(input('What is your XP progress number on this tier?'))
response_dict['Tier Goal'] = int(input('What number Tier is your goal?'))
response_dict['Daily Done'] = input('Is your Daily Done? y/n')
response_dict['Weekly Done'] = input('Is your Weekly Done? y/n')


from datetime import date, datetime
# Season end date and days remaining
bp_end = date(2021, 6, 22)
bp_start = date.today()
days = bp_end - bp_start
days_remaining = days.days

# Base experience constants
tier50xp = sum((i*750)+500 for i in list(range(51))) #981750
tiergoalxp = sum((i*750)+500 for i in list(range((response_dict['Tier Goal'] + 1))))
cum_exp = sum((i*750)+500 for i in list(range((response_dict['Tier'] + 1))))
remaining = tiergoalxp - (cum_exp + response_dict['Tier XP Progress'])

# exp split over time 
weekxp = remaining / 7
dayxp = remaining / days_remaining

# Weeklies exp creep:
wexp_start = 12000
wexp_end = 22000
wexp_week_inc = 1250

def main():
    if response_dict['Daily Done'] == 'n' and response_dict['Weekly Done'] == 'n':
        print('\n', '\n', '\n')
        print('Results:', '\n', '---------------------')
        print(f"Current XP = {cum_exp + response_dict['Tier XP Progress']}")
        print(f'BattlePass Total XP: {tiergoalxp}')
        print(f'Remaining XP = {remaining}' '\n', '\n')
        print(f"Remaining Tiers = {response_dict['Tier Goal'] - (response_dict['Tier']-1)}")
        print(f'Remaining Time = {days_remaining} Days')
        print(f'XP Needed per day = {round(dayxp)}')
        print(f'XP Needed per Week = {round(weekxp)}')
    
if __name__ == '__main__':
    main()
