"""
Lucas Lee, Zhaoyu Lin
SoftDev
k06 -- A Program to Print a Weighted Random Occupations From a CSV File
2021-09-29
"""

# SUMMARY OF TRIO DISCUSSION
# Read documentation for the csv module and used it to parse the csv given
# Skipped the header and the final total line
# Used the random module to weight the random choice based on the percentage of each job
# DISCOVERIES
# How to parse a csv file and manage/loop through entries in a dictionary
# How to weight a random selection based on a list of weights
# QUESTIONS
# What should be done about the 0.2% missing from the CSV?
# COMMENTS
# N/A

import csv
import random

def read_occupations(filename):

    dict = {}
    with open(filename) as f:
         lines = csv.reader(f, delimiter=',')
         next(lines) # Skips the header of the csv

         for line in lines: # Loops through each line of the csv
             job = line[0]
             percentage = float(line[1]) # Converts string to a number

             dict[job] = percentage # Crates a new dict entry with the job and percentage

    del dict['Total'] # Removes the sum of all the percentages

    return dict

def get_random_occupation(dict):

    # Chooses a random key using the values as weights
    # Returns a list with one element
    choice = random.choices(list(dict.keys()), weights = list(dict.values()), k = 1)

    return choice[0] # Picks out the first element


def main():
    occupations = read_occupations('occupations.csv')
    choice = get_random_occupation(occupations)

    print(choice)

if __name__ == '__main__':
    main()
