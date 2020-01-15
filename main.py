from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

def main():
    print('Parsing document...')

    periods = []
    skipped = 0

    tree = parse_schedule_html_file("data/202001.html")
    course_rows = tree.xpath('/html/body/div/div/center/descendant::table/tbody/tr')
    for tr in course_rows:
        # Remove non period rows
        if len(tr.xpath('th')) > 0:
            continue
        
        try:
            period = parse_html_period_row(tr)
            periods.append(period)
            print(period)
        except (IndexError, PeriodError) as e:
            # Invalid row!
            skipped += 1

    print(f'Done! Found {len(periods)} periods and skipped {skipped}')
if __name__ == "__main__":
    main()