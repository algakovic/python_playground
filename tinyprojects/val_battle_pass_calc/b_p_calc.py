#!/usr/bin/env python

'''
Author: ArkSealand
Date: 11.06.2021
Purpose: Valorant Battle Pass Calculator 
'''
import os

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