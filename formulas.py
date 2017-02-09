#Drew Guyer 2017
#Work checker, python practice script, and homework helper for calculus class
#Attempts to disuse math import when possible
###############################################################################
import functools
import math

def twopoints_tolinear(x1, y1, x2, y2):
    """ prints solutions for turning two points into linear equations.

    Args:
        x1, y1 = point one
        x2, y2 = point two

    Notes: nothing is reduced, and fractions are in decimal format
    """

    slope = "(%s/%s)" % (str(y2-y1),str(x2-x1))
    siformtemp = ((y2-y1/x2-x1)*x1)-y1

    print "Slope: %s" % slope
    print "Point-slope form: y-%s = %s(x-%s)" % (y1, slope, x1)
    print "Slope-intercept form: y=%sx + %s  " %(slope,siformtemp)
    print "Standard form: do by hand,check results above for correct formatting"


def quadratic(a, b, c):
    """prints solutions for quadratic equations

    Args:
        a,b,c = coefficients; ax^2 + bx + c = 0
    Returns:
        returns the numbers of solutions (to satisfy flow control testing)
    """

    discriminent = (b**2 - 4*a*c)

    if discriminent < 0:
        print "This equation has no real solutions"
        return 0
    elif discriminent == 0:
        print "This equation has one real solution:"
        print(-b + (discriminent)**.5)/ (2*a)
        return 1
    else:
        print "This equation has two real solutions:"
        print("x1:  %s") % str((-b + (discriminent)**.5)/ (2*a))
        print("x2:  %s") % str((-b - (discriminent)**.5)/ (2*a))
        return 2

def comp_interest(famount, p, rate, xcomp, years):
    """Prints and returns solutions for future amount and princple for compound
    interest functions.

    Formula: famount = p(1+(rate/xcomp))**(xcomp*years))

    Args:
        famount = future amount of money once compounded
        p = principle(present value) of money
        rate = interest rate
        xcomp = times compounded per year
        years = at the end of this many years

    Returns: float solution for the desired problem type

    Notes: enter "x" for the target unknown variable
    """

    if famount == "x": #solves for famount
        print "The future amount is:"
        solution = p * (1.00+(rate/xcomp))**(xcomp*years)
    elif p == "x": #solves for principle p
        print "The principle is:"
        solution = famount/((1.00+(rate/xcomp))**(xcomp*years))
    else: #solves for years
        print "Years is:"
        solution = math.log((1.00+(rate/xcomp)),(famount-p))/rate

    print solution
    return solution

def cont_comp_interest(famount,p,rate,years):
    """prints and returns solution for continuous compound interest functions.

    Formula: A = p*e**(r*t) #e = Euler's number = base of the natural log

    Args:
        famount = future amount of money once compounded
        p = principle(present value) of money
        rate = interest rate
        years = at the end of this many years

    Returns: float solution for the desired problem type

    Notes: enter "x" for the unknown target variable
    """

    if famount == "x": #solves for future amount
        print "The future amount is:"
        solution = p * math.exp((rate*years))
    elif p == "x": #solves for principle
        print "The principle is:"
        solution = famount/math.exp((rate*years))
    elif rate == "x": #solves for interest rate
        print "The interest rate is:"
        solution = math.log(famount/p)/years
    else: #solves for years
        print "Years is:"
        solution = math.log(famount/p)/math.fabs(rate)

    print solution
    return solution


def variable_in_exp(base,x):
    """prints solution for equations in the form base**y = x, log(_base)x = y

    Args:
        base = base
        y = uknown independent variable
        x = known
    """

    y = 0
    done = False
    while(not done):
        if(base**y != x):
            y+=1
        else:
            done = True
            print "The solution for y is: %s" % y



###############################################################################
def main():
    #SAMPLE METHOD CALLS
    #twopoints_tolinear(4.00,9.00,10.00,3.00)
    #quadratic(4.00,6.00,9.00)
    #cont_comp_interest(4000.00,2000.00,"x", 9.00)
    #comp_interest("x",5000.00,.0475,12)
    #variable_in_exp(10,26)


    """Complicated spaghetti logic for one of the problem types

    start = comp_interest("x",2000.00,.2047, 1.00, 10.00)
    time = 0.1
    answer = 0
    while (answer <= 2.00*start):
        answer = comp_interest("x",2000.00,.2047, 1.00, time)
        time += 0.1
    time = time-10.00
    print "the answer is: %s" % time
    """



    """Complicated spaghetti logic for one of the problem types

    time = .10
    solution = 0
    while(solution <= 35000.00):
        solution = cont_compint("x",10000.00,.042,time) + cont_compint("x",10000.00,.054,time)
        time+=.10
    print "answer: %s" % time
    """


if __name__ == "__main__":
    main()
###############################################################################
