import statistics
import math

class MyCalc:
    def __init__(self):
        self.ans = 0
        self.test_num_list = []

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2

        return self.ans

    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2

        return self.ans

    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2

        return self.ans

    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2

        return self.ans
#ucid: dc648 date:13/03/2022
    def square(self, num1):
        if num1 == "ans":
            return self.square(self.ans)
        else:
            num1 = self._as_number(num1)
            self.ans = pow(num1,2)
        return self.ans
#ucid: dc648 date:13/03/2022
    def sroot(self, num1):
        num1 = self._as_number(_num_)
        r = math.sqrt(_num_)
        self.ans = float('%.10g' % r)
        return self.ans
#ucid: dc648 date:13/03/2022
    def mean(self, num1):
        a = list()
        self.a = a
        for x in range(len(num1)):
            self.a.append(num1[x])
        b = statistics.mean(self.a)
        return round(b, 5)
#ucid: dc648 date:13/03/2022
    def median(self, num1):
        a = list()
        self.a = a
        for x in range(len(num1)):
            self.a.append(num1[x])
        b = statistics.median(self.a)
        return round(b, 5)
#ucid: dc648 date:13/03/2022
    def mode(self,num1):
        a = list()
        self.a = a
        for x in range(len(num1)):
            self.a.append(num1[x])
        b = statistics.mode(self.a)
        return round(b, 5)
#ucid: dc648 date:13/03/2022
    def stdev(self, num1):
        a = list()
        self.a = a
        for x in range(len(num1)):
            self.a.append(num1[x])
        b = statistics.stdev(self.a)
        return round(b, 5)
#ucid: dc648 date:13/03/2022
    def variance(self, num1):
        a = list()
        self.a = a
        for x in range(len(num1)):
            self.a.append(num1[x])
        b = statistics.variance(self.a)
        return round(b, 5)



if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "square" in iSTR:
                    nums = iSTR.split("square")
                    r = calc.square(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "sroot" in iSTR:
                    nums = iSTR.split("sroot")
                    r = calc.sroot(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "mean" in iSTR:
                    nums = iSTR.split("mean")
                    c = (nums[0].split())
                    for i in range(0, len(c)):
                        c[i] = float(c[i])
                    r = calc.mean(c)
                    print("R is" + str(r))
                elif "median" in iSTR:
                    nums = iSTR.split("median")
                    c = (nums[0].split())
                    for i in range(0, len(c)):
                        c[i] = float(c[i])
                    r = calc.median(c)
                    print("R is" + str(r))
                elif "mode" in iSTR:
                    nums = iSTR.split("mode")
                    c = (nums[0].split())
                    for i in range(0, len(c)):
                        c[i] = float(c[i])
                    r = calc.mode(c)
                    print("R is" + str(r))
                elif "stdev" in iSTR:
                    nums = iSTR.split("stdev")
                    c = (nums[0].split())
                    for i in range(0, len(c)):
                        c[i] = float(c[i])
                    r = calc.stdev(c)
                    print("R is" + str(r))
                elif "variance" in iSTR:
                    nums = iSTR.split("variance")
                    c = (nums[0].split())
                    for i in range(0, len(c)):
                        c[i] = float(c[i])
                    r = calc.variance(c)
                    print("R is" + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))



    else:
        print("Good bye")
        is_running = False

