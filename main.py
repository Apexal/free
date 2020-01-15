from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

EARLIST_TIME = '08:00'
LATEST_TIME = '19:00'

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

    for day in range(1, 6):
        print(f'Getting periods on day {day}')

        day_periods = sorted(list(filter(lambda p: day in p.days, all_periods)), key=lambda p: p.start_time)
        for period in day_periods:
            print(period)
        print()

if __name__ == "__main__":
    main()