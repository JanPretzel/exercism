class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.correct_display()

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hours, self.minutes)

    def __eq__(self, other):
        return str(self) == str(other)

    def add(self, minutes):
        self.minutes += minutes
        self.correct_display()
        return self

    def correct_display(self):
        self.hours += int(self.minutes / 60)
        if self.minutes < 0:
            self.hours -= 1
        self.hours %= 24
        self.minutes %= 60
