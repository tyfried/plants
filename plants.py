import datetime
import pdb
import json
import re
from tabulate import tabulate

def add_to_schedule(schedule,plant,day):
    if not schedule[day]:
        schedule[day] = plant
    else:
        schedule[day] += ", "+plant

def next_monday():
    days_ahead = 7 - datetime.datetime.now().weekday()
    return datetime.datetime.now() + datetime.timedelta(days_ahead)

def scheduler(file):
    with open(file) as json_file:
        plants = json.load(json_file)

    schedule = [None] * 12*7
    for plant in plants:
        wa = plant['water_after']
        match = re.match(r'(\d+)\sdays',wa)
        wa = int(match[1])
        for day in range(0,12*7):
            if day == 0:
                add_to_schedule(schedule,plant['name'],day)
            elif day % wa == 0:
                if day % 7 == 5:
                    add_to_schedule(schedule,plant['name'],day-1)
                elif day % 7 == 6:
                    add_to_schedule(schedule,plant['name'],day+1)
                else:
                    add_to_schedule(schedule,plant['name'],day)

    monday = next_monday()
    for i in range(0,12*7):
        schedule[i] = [(monday+datetime.timedelta(i)).strftime('%A, %m/%d/%Y'),schedule[i]]
    print(tabulate(schedule,headers=['Date','Plants']))



if __name__ == '__main__':
    # scheduler(sys.argv[1])
    scheduler('Apprentice_WeGrowInTandem_Data.json')
