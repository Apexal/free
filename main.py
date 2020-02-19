from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

START_HOURS = 8
END_HOURS = 19

def get_crns():
    with open('data/crns.txt') as f:
        return set(line.strip() for line in f.readlines())

def get_periods(term_code, crns):
    print('Parsing document...')

    print(f'Searching for {len(crns)} CRNs...')
    
    periods, _ = parse_schedule_html_file(f'data/{term_code}.html', crns)
    print(f'Done! Found {len(periods)} periods')

    return periods