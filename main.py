from course import Course
from parsing import parse_schedule_html_file, parse_html_period_row

def main():
    print('Parsing document...')

    periods = []

    tree = parse_schedule_html_file("data/202001.html")
    course_rows = tree.xpath('/html/body/div/div/center/descendant::table/tbody/tr')
    for tr in course_rows:
        # Remove non period rows
        if len(tr.xpath('th')) > 0:
            continue
        
        try:
            period = parse_html_period_row(tr)
            periods.append(period)
        except:
            # Invalid row!
            pass

    print(f'Done! Found {len(periods)} periods')
if __name__ == "__main__":
    main()