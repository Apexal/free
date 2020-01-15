from lxml import html
from period import Period, PeriodError

def parse_schedule_html_file(filename):
  '''
  Read and parse a valid schedule HTML file from the registrar. 
  
  Parameters:
  filename (str): the location of the HTML file

  Returns:
  lxml HTML tree
  '''
  with open(filename) as f:
    tree = html.fromstring(f.read())
    return tree

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

def parse_html_period_row(tr):
  '''
  Creates a Period from a table row.
  '''
 
  ptype = get_td_text(tr, 3)
  if len(ptype) < 3:
    ptype = "???"

  # If days are empty, then we do not care about this period.
  days = list(filter(lambda s: len(s) > 0 and s != " ", get_td_text(tr, 6)))
  if len(days) == 0:
    raise PeriodError("Period days are empty.")

  start_time = get_td_text(tr, 7)
  end_time = get_td_text(tr, 8)
  location = tr.xpath('td[10]')[0].text_content().strip()

  return Period(
    ptype,
    days,
    start_time,
    end_time,
    location
  )
