#Drew Guyer 2017
#Work checker, python practice script, and homework helper for calculus class
#Attempts to disuse math import when possible
###############################################################################
import math


def quadratic(a, b, c):
    """prints solutions for quadratic equations

    Args:
        a,b,c = coefficients; ax^2 + bx + c = 0
    """

    discriminent = (b**2 - 4*a*c)

    if discriminent < 0:
        print "This equation has no real solutions"
    elif discriminent ==0:
        print "This equation has one real solution:"
        print(-b + (discriminent)**.5)/ (2*a)
    else:
        print "This equation has two real solutions:"
        print("x1:  %s") % str((-b + (discriminent)**.5)/ (2*a))
        print("x2:  %s") % str((-b - (discriminent)**.5)/ (2*a))

def comp_interest(famount, p, rate, xcomp, years):
    """prints solutions for future amount and princple for compound interest
       functions.

    Formula: famount = p(1+(rate/xcomp))**(xcomp*years))

    Args:
        famount = future amount of money once compounded
        p = principle(present value) of money
        rate = interest rate
        xcomp = times compounded per year
        years = at the end of this many years
    """

    if famount == "x": #solves for famount
        solution = p*(1.00+(rate/xcomp))**(xcomp*years)
    else: #solves for principle p
        solution = famount/((1.00+(rate/xcomp))**(xcomp*years))

    print solution

def cont_compint(famount,p,rate,years):
    """prints solution for continuous compound interest functions.

    Formula: A = p*e**(r*t) #e = Euler's number = base of the natural log

    Args:
        famount = future amount of money once compounded
        p = principle(present value) of money
        rate = interest rate
        years = at the end of this many years
    """

    if famount == "x":
        print "The future amount is:"
        solution = p* math.exp((rate*years))
    elif p == "x":
        print "The principle is:"
        solution = famount/math.exp((rate*years))
    else:
        print "Years need is:"
        solution = math.log(famount/p)/rate

    print solution


def variable_in_exp(base,x):
    """prints solution for equations in the form base**y = x, log(_base)x = y

    Args:
        base = base
        y = uknown independent variable
        x = known
    """

    y = 1
    done = False
    while(not done):
        if(base**y != x):
            y+=1
        else:
            done = True
            print "The solution for y is: %s" % y


###############################################################################
def main():
    #quadratic(4.00,6.00,9.00)
    #comp_interest("x",10000.00,.02, 12.00, 5.00)
    cont_compint(75000.00, 30000.00, .0491,"x")
    #variable_in_exp(8,64)

if __name__ == "__main__":
    main()
###############################################################################
