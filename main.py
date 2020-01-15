from parsing import parse_schedule_html_file, parse_html_period_row
from period import PeriodError

def main():
    print('Parsing document...')

    skipped = 0

    # {crn: [periods]}
    periods = {}

    tree = parse_schedule_html_file("data/202001.html")
    course_rows = tree.xpath('/html/body/div/div/center/descendant::table/tbody/tr')
    crn = None
    for tr in course_rows:
        # Remove non period rows
        if len(tr.xpath('th')) > 0:
            continue
        
        # Get crn if exists
        try:
            crn = tr.xpath('td[1]')[0].text_content().strip().split()[0]
        except:
            pass
        
        # Attempt to parse the row as a Period, if an exception is thrown, the row must not be a valid period and is skipped
        try:
            period = parse_html_period_row(tr)

            if not crn in periods:
                periods[crn] = []
            
            periods[crn].append(period)
        except (ValueError, IndexError, PeriodError) as e:
            # Invalid row!
            print(e)
            skipped += 1

    # Print results
    for crn in periods:
        print(crn)
        for period in periods[crn]:
            print(period)
        print()

    print(f'Done! Found {len(periods)} courses and skipped {skipped}')

if __name__ == "__main__":
    main()