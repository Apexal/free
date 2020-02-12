from lxml import html
from period import Period, PeriodError

TIME_FORMAT = '%H:%M'

DAY_NUMS = {
    'M': 1,
    'T': 2,
    'W': 3,
    'R': 4,
    'F': 5
}

course_summaries = {}

def parse_schedule_html_file(filename, crns):
    '''
    Read and parse a valid schedule HTML file from the registrar. 

    Parameters:
    filename (str): the location of the HTML file

    Returns:
    lxml HTML tree
    '''
    with open(filename) as f:
        tree = html.fromstring(f.read())

    periods = []
    skipped = 0

    course_rows = tree.xpath(
        '/html/body/div/div/center/descendant::table/tbody/tr')
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
            period = parse_html_period_row(tr, crn)

            if crn in crns:
                periods.append(period)
        except (ValueError, IndexError, PeriodError) as e:
            # Invalid row!
            skipped += 1

    return periods, skipped


def get_td_text(tr, index):
    '''
    Gets the text of a specific child td in a tr element.

    Parameters:
    tr (lxml element): The parent table row
    index (int): The index of the child td to get the text of

    Returns:
    str: The stripped text of the specified td
    '''
    return tr.xpath(f'td[{index}]')[0].text_content().strip()


def determine_times(start_time, end_time):
    start_hours, start_minutes = [int(n) for n in start_time.split(':')]
    end_hours, end_minutes = [int(n) for n in end_time.replace(
        'AM', '').replace('PM', '').split(':')]

    # Possible change in meridiem
    if 'PM' in end_time:
        if end_hours < 12:
            end_hours += 12
        if start_hours + 12 <= end_hours:
            start_hours += 12

    return f'{start_hours:02}:{start_minutes:02}', f'{end_hours:02}:{end_minutes:02}'


def parse_html_period_row(tr, crn):
    '''
    Creates a Period from a table row.
    '''

    ptype = get_td_text(tr, 3)
    if len(ptype) < 3:
        ptype = "???"

    # If days are empty, then we do not care about this period.
    days = list(map(lambda s: DAY_NUMS[s], filter(
        lambda s: len(s) > 0 and s != " ", get_td_text(tr, 6))))
    if len(days) == 0:
        raise PeriodError("Period days are empty.")

    course_summary = ''.join(get_td_text(tr, 1).split()[1:]).strip()
    if len(course_summary) > 0:
        course_summaries[crn] = course_summary
    else:
        course_summary = course_summaries[crn]

    # 9:00 or 10:00
    # Convert from H:MM to HH:MM
    start_time, end_time = determine_times(
        get_td_text(tr, 7), get_td_text(tr, 8))

    location = tr.xpath('td[10]')[0].text_content().strip()

    return Period(
        crn,
        course_summary,
        ptype,
        days,
        start_time,
        end_time,
        location
    )
