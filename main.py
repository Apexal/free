from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

def main():
    print('Parsing document...')

    # {crn: [periods]}
    periods, skipped = parse_schedule_html_file('data/202001.html')

    # Print results
    for crn in periods:
        print(crn)
        for period in periods[crn]:
            print(period)
        print()

    print(f'Done! Found {len(periods)} courses and skipped {skipped}')

if __name__ == "__main__":
    main()