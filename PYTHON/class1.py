class dev:
    raised_amt = 1.40
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = name + last + "@gmail.com"
    def fullname(self):
        return '{} {}'.format(self.name, self.last)
    def inc_pay(self):
        return int(self.pay * self.raised_amt)

dev_1 = dev("Pritam", "Dey", 150000)
dev_2 = dev("Jayati", "Mahoto", 15000)
print(dev_1.pay)
print(dev_1.fullname())
print(dev_1.inc_pay())