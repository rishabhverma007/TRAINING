class dev:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = name + last + "@gmail.com"
    def fullname():
        return '{} {}'.format(dev_1.name, dev_1.last)    

dev_1 = dev("Pritam", "Dey", 150000)
dev_2 = dev("Jayati", "Mahoto", 15000)

print(dev_1.name)
print(dev_2.name)
