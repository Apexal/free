class Course:
    def __init__(self, crn, summary, title):
        self.crn = crn
        self.summary = summary
        self.title = title

class Period:
    def __init__(self, ptype, days, start_time, end_time, location='TBD'):
        self.start_time = start_time
        self.ptype = ptype
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    @property
    def duration(self):
        # TODO: calculate
        return -1

    def __str__(self):
        return f'{self.ptype} period on days {self.days} at location {self.location} from {self.start_time} to {self.end_time}'

class PeriodError(RuntimeError):
    def __init__(self, arg):
      self.args = arg