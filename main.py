from parsing import parse_schedule_html_file, parse_html_period_row

def get_crns():
    with open('data/crns.txt') as f:
        return set(line.strip() for line in f.readlines())

def main():
    print('Parsing document...')

    crns = get_crns()
    print(f'Searching for {len(crns)} CRNs...')
    periods = []

    tree = parse_schedule_html_file('data/202001.html')
    course_rows = tree.xpath('/html/body/div/div/center/descendant::table/tbody/tr')
    for tr in course_rows:
        # Remove non period rows
        if len(tr.xpath('th')) > 0:
            continue
        
        try:
            period = parse_html_period_row(tr)
            if period.crn in crns:
                print(f'Found course {period.course_title}')
                periods.append(period)
        except Exception as e:
            # print(e)
            # Invalid row!
            pass

    print(f'Done! Found {len(periods)} periods')

if __name__ == '__main__':
    main()