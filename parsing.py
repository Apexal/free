from lxml import html
from period import Period

def parse_schedule_html_file(filename):
  with open(filename) as f:
    tree = html.fromstring(f.read())
    return tree

def parse_html_period_row(tr):
  # '92556 STSH-1110-01' -> ['92556', 'STSH-1110-01']
  [crn, summary] = tr.xpath('td[1]/span/text()')[0].strip().split()

  return Period(
    crn,
    summary,
    tr.xpath('td[3]/span')[0].text_content().strip(),
    ['M', 'F'],
    '00:00',
    '00:00'
  )