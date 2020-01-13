class Course:
    def __init__(self, title, crn, section, periods=[]):
        self.title = title
        self.crn = crn
        self.section = section
        self.periods = periods

    @property
    def summary(self):
        return f'{self.title} - {self.section}'
        