from course import Course
from period import Period
from parsing import parse_schedule_html_file

def main():
    print("Parsing document...")
    tree = parse_schedule_html_file("data/202001.html")
    print("Done!")

if __name__ == "__main__":
    main()