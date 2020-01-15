from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

START_HOURS = 8
END_HOURS = 19

def main():
    print('Parsing document...')

    # {crn: [periods]}
    periods, skipped = parse_schedule_html_file('data/202001.html')
    all_periods = [item for sublist in periods.values() for item in sublist]
    # # Print results
    # for crn in periods:
    #     print(crn)
    #     for period in periods[crn]:
    #         print(period)
    #     print()

    print(f'Done! Found {len(periods)} courses and skipped {skipped}')

    all_slots = {}

    for day in range(1, 6):
        min_start_time = END_HOURS-1
        day_slots = {}

        for hour in range(START_HOURS, END_HOURS):
            day_slots[(hour, hour+1)] = 0
        
        
        print(f'Getting periods on day {day}')

        day_periods = sorted(list(filter(lambda p: day in p.days, all_periods)), key=lambda p: p.start_time)
        for period in day_periods:
            # Check if period falls within an hour slot
            for start_hour, end_hour in day_slots:
                if start_hour <= period.start_hour:
                    day_slots[(start_hour, end_hour)] += 1

                if day_slots[(start_hour, end_hour)] < day_slots[(min_start_time, min_start_time+1)]:
                    min_start_time = start_hour

        all_slots[day] = day_slots
        print("BEST HOUR TO START FOR", day, "IS", min_start_time, "with", day_slots[(min_start_time, min_start_time+1)])
    
    # print(all_slots)

if __name__ == "__main__":
    main()