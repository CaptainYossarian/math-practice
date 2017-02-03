#Drew Guyer 2017
#Work checker, python practice script, and homework helper for calculus class
#Attempts to disuse math import when possible
###############################################################################
import math

def quadratic(a, b, c):
    """returns solutions for quadratic equations

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
    return "Work checked."

def comp_interest(famount, p, rate, xcomp, years):
    """returns solutions for future amount and princple for compound interest
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
        print solution
    else: #solves for principle p
        solution = famount/((1.00+(rate/xcomp))**(xcomp*years))
        print solution

def continuous_compint(p,rate,years):
    """returns solution for continuous compound interest functions.

    Formula: A = p*e**(r*t) #e = Euler's number = base of the natural log

    Args:
        p = principle(present value) of money
        rate = interest rate
        years = at the end of this many years
    """

    solution = p* math.exp((rate*years))
    print solution


###############################################################################
def main():
    #comp_interest("x",7300.00,.059, 12.00, 8.00)
    #continuous_compint(25000.00,.0455, 11)

if __name__ == "__main__":
    main()
###############################################################################
