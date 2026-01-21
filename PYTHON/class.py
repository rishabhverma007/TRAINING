class gadhe:
    def __init__(self, quality, weight):
        self.quality = quality
        self.weight = weight
g1 = gadhe("good", 500)
g2 = gadhe("bad", 300)

print(g1.quality)
print(g2.weight)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks>=60:
            return "Pass"
        else:
            return "Fail"
s = Student("Ravi",55)
print(s.result())