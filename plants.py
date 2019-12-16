import datetime
import pdb
import json
import re
import sys
from tabulate import tabulate


def next_monday():
    """
    Return 'next monday' as a datetime.
    """
    days_ahead = 7 - datetime.datetime.now().weekday()
    return datetime.datetime.now() + datetime.timedelta(days_ahead)

def assign(schedule,name,day):
    """
    Assign plant to schedule on given day.
    """
    if not schedule[day]:
        schedule[day] = name
    else:
        schedule[day] += ", "+name

def scheduler(plants,schedule):
    """
    For each plant, assign its watering days to the schedule.
    """
    for plant in plants:

        ## Convert water_after to integer.
        water_after = plant['water_after']
        match = re.match(r'(\d+)\sdays',water_after)
        water_after = int(match[1])

        ## Loop through all desired watering days, correcting for weekends.
        for day in range(0,12*7,water_after):
            if day % 7 == 5:
                assign(schedule,plant['name'],day-1)
            elif day % 7 == 6 and day != 12*7-1:
                assign(schedule,plant['name'],day+1)
            else:
                assign(schedule,plant['name'],day)

def plants(file):

    ## Open the file.
    with open(file) as json_file:
        plants = json.load(json_file)

    ## Assign days to the schedule.
    schedule = [None] * 12*7
    scheduler(plants,schedule)


    ## Convert each day to the appropriate date string relative to "next monday".
    monday = next_monday()
    for i in range(0,12*7):
        schedule[i] = [(monday+datetime.timedelta(i)).strftime('%A, %m/%d/%Y'),schedule[i]]

    ## Pretty print using tabulate.
    print(tabulate(schedule,headers=['Date','Plants']))

if __name__ == '__main__':
    plants(sys.argv[1])
