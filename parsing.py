from lxml import html

def parse_schedule_html_file(filename):
  with open(filename) as f:
    tree = html.fromstring(f.read())
    return tree