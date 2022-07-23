# dictionary of activities of the week
def run():
    weekdays ={
        'Monday' :'Make 100 push ups',
        'Tuesday' : 'Run 10km',
        'Wednesday' : 'Make 100 crunches',
        'Thursday' : 'Swim 5 km',
        'Friday' : 'Run 15 km',
        'Saturday' : 'Cycling 32 km',
        'Sunday' : 'Rest and eat pizza'
    }
    for day, activity in weekdays.items():
        print('On ' + day + ' the activity is: ' + activity)


if __name__ == '__main__':
    run()