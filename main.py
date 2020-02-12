from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError
from timing import form_schedule, fill_schedule

START_HOURS = 8
END_HOURS = 19

def get_crns():
    with open('data/crns.txt') as f:
        return set(line.strip() for line in f.readlines())

def main():
    print('Parsing document...')

    crns = get_crns()
    print(f'Searching for {len(crns)} CRNs...')
    
    periods, _ = parse_schedule_html_file('data/202001.html', crns)
    # for period in periods:
    #     print(period)
    #     print()
    print(f'Done! Found {len(periods)} periods')

    schedule = form_schedule()
    fill_schedule(schedule, periods)

    for day in range(1,6):
        print(day)
        for hour_block in schedule[day]:
            print(hour_block, schedule[day][hour_block])

if __name__ == '__main__':
    main()