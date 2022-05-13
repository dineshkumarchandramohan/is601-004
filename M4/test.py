import statistics
def median(self, num1):
    a = list()
    self.a = a
    for x in range(len(num1)):
        self.a.append(num1[x])
        print(a)
    b = statistics.median(self.a)
    return round(b, 5)

val1 = ['1,2,3,4,5,6,7,8,9,10']
