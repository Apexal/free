START_HOUR = 8
END_HOUR = 22
DAYS = ['M', 'T', 'W', 'T', 'F']

def form_schedule():
    '''
    Generate a 5-day (M-F) schedule split into hour long blocks from START_HOUR to END_HOUR
    '''
    hour_blocks = {}
    for start_hour in range(START_HOUR, END_HOUR):
        hour_block = (start_hour, start_hour+1)
        hour_blocks[hour_block] = 0

    schedule = {}
    for day in range(1, 6):        
        schedule[day] = hour_blocks.copy()

    return schedule

def fill_schedule(schedule, periods):
    for day in range(1, 6):
        hour_blocks = schedule[day]

        for hour_block in hour_blocks:
            # Find number of periods that are in session during this hour block
            def in_session(period):
                # hour_block = (9, 10)
                # period times = (8, 10)
                answ = period.start_hour <= hour_block[0] and period.end_hour >= hour_block[1]
                
                # print(f'{period.start_time}-{period.end_time} ({period.start_hour}, {period.end_hour}) vs {hour_block}: {answ}')
                return answ

            in_session = filter(in_session, periods)
            schedule[day][hour_block] = len(list(in_session))
    
    return schedule