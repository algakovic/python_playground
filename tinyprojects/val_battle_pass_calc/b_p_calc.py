#!/usr/bin/env python

'''
Author: ArkSealand
Date: 11.06.2021
Purpose: Valorant Battle Pass Calculator 
'''
import os
from datetime import date

'''
Steps:
1. Input user Questions
    - what tier is the User on?
    - How much progress does it have?
    - Have you done your daily?
    - What is the Start Date (todays date)?
    - Specify an end date default is season end.
    - Include this weeks weekly?

2. Response
    - conditional flow
    - returns current xp
        - xp needed per day
        - xp needed per week
        - remaining tiers
        - remaining time 
        - table of useful timeframes for spike /dm /unrated
''' 

def main():
    response_dict = {}
    response_dict['Tier'] = input('What number Tier are you currently on?')
    response_dict['Tier XP Progress'] = input('What is your XP progress number on this tier?')
    response_dict['Tier Goal?'] = input('What number Tier is your goal?')
    response_dict['Daily Done'] = input('Is your Daily Done? Y/N')
    response_dict['Weekly Done'] = input('Is your Weekly Done? Y/N')
    response_dict['date Today'] = date.today().strftime("%d/%m/%Y")
    
    return print(response_dict)

if __name__ == '__main__':
    main()
