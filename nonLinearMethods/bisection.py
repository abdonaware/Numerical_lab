from sympy import *
import time
import math

class Bisection:

    def __init__(self):
        self.res = 0
        self.time = 0.0
        self.iterations = 0
        self.error = 0
        self.correctSF = 0
        self.steps = ""

    def getSolution (self):
        return self.res
      
    def getExcutionTime (self):
        return self.time
    
    def getIterations (self):
        return self.iterations

    def getError (self):
        return self.error
    
    def getcorrectSF (self):
        return self.correctSF
    
    def getSteps(self):
        return self.steps

    def solve(self,func,a, b, tolerance,max_iterations, SF):
        x = a
        prev_x = 0  
        error = 1
        counter = 0
        start_time = time.time()
        self.steps += " i \t Xl \t Xu \t Xr \t εt %"
        while ( error >= tolerance and counter<=max_iterations):
            prev_x = x
            x = (a + b) / 2
            x = round(x,SF)
            counter+=1
            if(x != 0):
                error = abs((x - prev_x)) / x
            signn = "(+)"
            if(func(x) < 0):
                signn = "(-)"
            self.steps += f" \n {counter} \t {a} \t {b} \t {x} \t {signn} \t {error*100}"

            if func(x) == 0:  
                break

            if func(x) * func(a) < 0:
                b = x
            else:
                a = x


        try:
            self.correctSF = math.floor(2-math.log10(error/0.5))
        except ValueError as e:
            self.correctSF = float('inf')

        self.error = error*100
        end_time = time.time()
        self.time = end_time - start_time
        self.iterations = counter
        self.res = f"%{SF/10}f" % x




x = symbols('x')
expr_str = "x**3-x-1"
expr = sympify(expr_str)
func = lambdify(x, expr)

b = Bisection()
b.solve(func,1,2,1e-4,100,5)
print(b.getSteps())