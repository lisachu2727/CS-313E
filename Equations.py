#File: Equations.py
#Description: HW1
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 2/3/2019
#Date Last Modified: 2/6/2019 

class LinearEquation:
    def __init__(self,m,b):
        #in the form of y = mx + b, where m is slope and b is intercept
        self.m = m
        self.b = b
        
    def __str__(self):
        #if statements divided up with respect to m and b
        
        #assigning sign, variable, and number for different situations of m
        if self.m == 1:
            mSign = ' '
            mVariable = 'x'
            m = ''
        elif self.m > 0:
            mSign = ' '
            mVariable = 'x'
            m = abs(self.m)
        elif self.m < 0:
            mSign = ' - '
            mVariable = 'x'
            m = abs(self.m)
        else:
            mSign = ''
            mVariable = ''
            m = ''

        #assigning sign and number for different situations of b

        #testing if a plus sign is needed in front of b by testing if there is
            #anything in front of b
        if self.b > 0 and mVariable == 'x':
            bSign = ' + '
            b = abs(self.b)
        elif self.b > 0 and mVariable != 'x':
            bSign = ''
            b = abs(self.b)
        elif self.b < 0:
            bSign = ' - '
            b = abs(self.b)
        else:
            bSign = ''
            b = ''

        #putting together sign, number, variable, sign, number
        return mSign + str(m) + mVariable + bSign + str(b)

    #solving linear equation with variable x substituted for a number
    def evaluate(self,x):
        return (self.m * x) + self.b

    #adding two linear equations together
    def __add__(self,otherLE):
        newM = self.m + otherLE.m
        newB = self.b + otherLE.b
        
        return LinearEquation(newM,newB)

    #subtracting two linear equations together
    def __sub__(self,otherLE):
        newM = self.m - otherLE.m
        newB = self.b - otherLE.b
        
        return LinearEquation(newM,newB)

    #multiplying two linear equations together, creating a quadratic equation
    def __mul__(self,otherLE):
        a = self.m * otherLE.m
        b = (self.m * otherLE.b) + (self.b * otherLE.m)
        c = self.b * otherLE.b
        
        return QuadraticEquation(a,b,c)

    #performing composition of linear equations
    def compose(self,otherLE):
        newM = self.m * otherLE.m
        newB = (self.m * otherLE.b) + self.b
        
        return LinearEquation(newM,newB)

class QuadraticEquation:
    def __init__(self,a,b,c):
        #in the form of y = ax² + bx + c, where a, b, and c are constants
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        #if statements divided up with respect to a, b, and c

        #assigning sign, variable, and number for different situations of a
        if self.a == 1:
            aSign = ' '
            aVariable = 'x\u00B2'
            a = ''    
        elif self.a > 0:
            aSign = ' '
            aVariable = 'x\u00B2'
            a = self.a
        elif self.a == -1:
            aSign = ' - '
            aVariable = 'x\u00B2'
            a = ''
        elif self.a < 0:
            aSign = ' - '
            aVariable = 'x\u00B2'
            a = abs(self.a)
        else:
            aSign = ''
            aVariable = ''
            a = ''

        #assigning sign, variable, and number for different situations of b

        #testing if a plus sign is needed in front of b by testing if there is
            #anything in front of b
        if self.b == 1 and aVariable == 'x\u00B2':
            bSign = ' + '
            bVariable = 'x'
            b = ''
        elif self.b > 0 and aVariable == 'x\u00B2':
            bSign = ' + '
            bVariable = 'x'
            b = abs(self.b)
        elif self.b > 0 and aVariable != 'x\u00B2':
            bSign = ''
            bVariable = 'x'
            b = abs(self.b)
        elif self.b == -1:
            bSign = ' - '
            bVariable = 'x'
            b= ''
        elif self.b < 0:
            bSign = ' - '
            bVariable = 'x'
            b = abs(self.b)
        else:
            bSign = ''
            bVariable = ''
            b = ''

        #assigning sign, number, and variable for different situations of c

        #testing if a plus sign is needed in front of c by testing if there is
            #anything in front of c
        if self.c == 1 and (aVariable == 'x\u00B2' or bVariable == 'x'):
            cSign = ' + '
            c = ''
        elif self.c > 0 and (aVariable == 'x\u00B2' or bVariable == 'x'):
            cSign = ' + '
            c = abs(self.c)
        elif self.c > 0 and (aVariable != 'x\u00B2' and bVariable != 'x'):
            cSign = ''
            c = abs(self.c)
        elif self.c == -1:
            cSign = ' - '
            c = ''
        elif self.c < 0:
            cSign = ' - '
            c = abs(self.c)
        else:
            cSign = ''
            c = ''

        #putting together all signs, variables, and numbers
        return aSign + str(a) + aVariable + bSign + str(b) + bVariable + \
               cSign + str(c)

    #solving quadratic equation with variable x substituted for a number   
    def evaluate(self,x):
        return (self.a * x * x) + (self.b * x) + self.c

    #adding two quadratic equations together
    def __add__(self,otherQE):
        newA = self.a + otherQE.a
        newB = self.b + otherQE.b
        newC = self.c + otherQE.c
        
        return QuadraticEquation(newA,newB,newC)

    #subtracting two quadratic equations together
    def __sub__(self,otherQE):
        newA = self.a - otherQE.a
        newB = self.b - otherQE.b
        newC = self.c - otherQE.c
        
        return QuadraticEquation(newA,newB,newC)

def main():

   f = LinearEquation(5,3)
   print("f(x) =",f)
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("k(x) = f(g(x)) =",k,"\n")
   
   m = g.compose(f)
   print("m(x) = g(f(x)) =",m,"\n")

   n = f * g
   print("n(x) = f(x) * g(x) =",n,"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g)
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f + g
   print("h(x) = f(x) + g(x) =",h)
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f - g
   print("j(x) = f(x) - g(x) =",j)
   print("j(-4) =",j.evaluate(-4),"\n")
   
   p = QuadraticEquation(1,1,-6)
   print("p(x) =",p)
   print("p(3) =",g.evaluate(3),"\n")
   
   q = QuadraticEquation(2,1,4)
   print("q(x) =",q)
   print("q(-3) =",q.evaluate(-3),"\n")
   
   r = p + q
   print("r(x) = p(x) + q(x) =",r)
   print("r(-2) =",r.evaluate(-2),"\n")

   s = p - q
   print("s(x) = p(x) - q(x) =",s)
   print("s(1) =",s.evaluate(1),"\n")
   
main()
