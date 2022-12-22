# To Create Time

class Time:
    def setTime(self, h, m=0):
        self.hours = h
        self.min = m

    def increment(self, i=1):
        hours = self.hours+i
        print("Time is", self.hours, ":", self.min, "and Hours is", hours)


a = Time()
a.setTime(2, 45)
a.increment()

b = Time()
b.setTime(7)
b.increment(1)
