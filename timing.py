START_HOUR = 8
END_HOUR = 22

def form_schedule(periods):
    '''
    Generate a 5-day (M-F) schedule split into hour long blocks
    '''
    days = []
    for day in range(1, 6):
        hours = []
        for start_hour in range(END_HOUR - START_HOUR):
            hour = (start_hour, start_hour+1)
            hours.append(hour)
        days.append(hours)
