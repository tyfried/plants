import datetime
import pdb
import json
import re
from tabulate import tabulate

def next_monday():
    days_ahead = 7 - datetime.datetime.now().weekday()
    return datetime.datetime.now() + datetime.timedelta(days_ahead)

def assign(schedule,name,day):
    if not schedule[day]:
        schedule[day] = name
    else:
        schedule[day] += ", "+name

def scheduler(plants,schedule):
    for plant in plants:
        water_after = plant['water_after']
        match = re.match(r'(\d+)\sdays',water_after)
        water_after = int(match[1])
        for day in range(0,12*7):
            if day == 0:
                assign(schedule,plant['name'],day)
            elif day % water_after == 0:
                if day % 7 == 5:
                    assign(schedule,plant['name'],day-1)
                elif day % 7 == 6 and day != 12*7-1:
                    assign(schedule,plant['name'],day+1)
                else:
                    assign(schedule,plant['name'],day)

def plants(file):
    with open(file) as json_file:
        plants = json.load(json_file)

    schedule = [None] * 12*7
    scheduler(plants,schedule)

    monday = next_monday()
    for i in range(0,12*7):
        schedule[i] = [(monday+datetime.timedelta(i)).strftime('%A, %m/%d/%Y'),schedule[i]]
    print(tabulate(schedule,headers=['Date','Plants']))



if __name__ == '__main__':
    scheduler(sys.argv[1])
    # plants('Apprentice_WeGrowInTandem_Data.json')
