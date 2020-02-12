from time import strftime, strptime

class Period:
    def __init__(self, crn, course_summary, ptype, days, start_time, end_time, location='TBD'):
        self.crn = crn
        self.course_summary = course_summary
        self.ptype = ptype
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    @property
    def duration(self):
        # TODO: calculate
        return -1

    @property
    def start_hour(self):
        return int(self.start_time.split(':')[0])
    
    @property
    def end_hour(self):
        return int(self.end_time.split(':')[0])

    def __str__(self):
        return f'{self.crn} {self.course_summary} {self.ptype} period on days {self.days} at location {self.location} from {self.start_time} to {self.end_time}'

    def __repr__(self):
        return self.__str__()

class PeriodError(RuntimeError):
    def __init__(self, arg):
      self.args = arg