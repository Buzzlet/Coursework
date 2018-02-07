# Program: fraction.py
# Class:   cs131
# Date:    11/21/14
# Author:  Joel Ristvedt

# Description: This program contains the class Fraction which holds attributes
# and methods for each Fraction object.

# Classes

class Fraction():

    def Find_GCD(self):
        """Finds the greatest common divisor of a fraction
           parameters:
           self - the fraction
           returns:
           divisor - the greatest common integer divisor
        """
        # remainder - the remainder of the numerator divided by the 
        #             denominator
        # divisor - a factor of both the numerator and denominator
        # numerator - new value of the numerator to run the check through with
        # denominator - new value of the denominator to run the check through
        #              with
        remainder = self.numerator % self.denominator
        if remainder == 0:
            divisor = self.denominator
        else:
            numerator = self.denominator
            denominator = remainder
            divisor = Fraction(numerator, denominator, False).Find_GCD()
        return divisor
            
            
    def Reduce(self):
        """Reduces a fraction to its simplest form
           parameters: 
           self - the fraction
           returns: none
        """
        # divisor - the largest factor of both the numerator and denominator
        divisor = self.Find_GCD()
        self.numerator = self.numerator // divisor
        self.denominator = self.denominator // divisor

    def Manage_Negative(self):
        """Determines what to do with negatives in a fraction
           parameters:
           self - the fraction
           returns: none
        """
        if self.denominator < 0 and self.numerator > 0:
            self.denominator = abs(self.denominator)
            self.numerator = self.numerator * -1
            if self.numerator < 0 and self.denominator < 0:
                self.numerator = abs(self.numerator)
                self.denominator = abs(self.denominator)

    def __init__(self, numerator=1, denominator=1, simplify=True):
        """Initilizes the attributes and stores the fraction in reduced form
           parameters:
           numerator - the number for the top of the fraction
           denominator - the number for the bottom of the fraction
           simplify - boolean toggle for whether to reduce fraction or not
           returns: none
        """
        self.numerator = numerator
        self.denominator = denominator
        self.Manage_Negative()
        if simplify == True:
            self.Reduce()

    def Assign(self, numerator, denominator):
        """Gives new values to an existing fraction
           self - the fraction
           numerator - new number for the top of the fraction
           denominator - new number for the bottom of the fraction
           returns: none
        """
        if denominator != 0:
            self.numerator = numerator
            self.denominator = denominator
            self.Reduce()
                    
    
    def Decimal(self):
        """Returns a decimal evaluation of a fraction
           parameters:
           self - the fraction
           returns: float
        """
        return self.numerator / self.denominator
    
    def To_String(self):
        """Returns a string of a fraction as a proper fraction
           parameters:
           self - the fraction
           returns:
           string - the final string representation of the fraction object
        """
        if abs(self.numerator) >= self.denominator:
            string = str(abs(self.numerator) // self.denominator)
            if self.numerator < 0:
                string = '-' + string 
            if abs(self.numerator) % self.denominator != 0:
                string += ( ' ' + str(abs(self.numerator) % self.denominator)
                          + '/' +str(self.denominator))    
        else:
            string = str(self.numerator) +'/'+ str(self.denominator)    
        
        if self.numerator == 0:
            string = '0'

        return string        
    
    def Print(self):
        """Prints a fraction with the numerator and denominator separated by
           a slash
           parameters:
           self - the fraction
           returns: none
           
        """
        print(self.numerator,'/',self.denominator,sep='',end='')

    def __add__(self, fraction):
        """Defines the conventions for adding a fraction to other fractions
           and integers
           parameters: 
           self - the fraction
           fraction - the second addend
           returns:
           result - a new fraction that is the sum of the addends
        """
        # numerator - the top of the new fraction
        # denominator - the bottom of the new fraction
        if type(fraction) == 'Integer':
            fraction = Fraction(fraction, 1)
        result = Fraction()
        if self.denominator == fraction.denominator:
            result.Assign(self.numerator + fraction.numerator,
                          fraction.denominator)
        else:
            numerator = self.numerator * fraction.denominator + (
                        fraction.numerator * self.denominator)
            denominator = self.denominator * fraction.denominator
            result.Assign(numerator, denominator)
        return result

    def __sub__(self, fraction):
        """Defines the conventions for subtracting a an integer or fraction
           from a fraction
           parameters:
           self - the fraction
           fraction - the second subtrahend
           returns:
           result - a new fraction that is the difference of the subtrahends
        """
        result = self + Fraction(-fraction.numerator, fraction.denominator)
        return result
    
    def __mul__(self, fraction):
        """Defines the conventions for multiplying a fraction with another 
           fraction or integer
           parameters:
           self - the fraction
           fraction - the second multiplicand
           returns:
           result - a new fraction that is the product of the multiplicands
        """
        # numerator - the top of the new fraction
        # denominator - the bottom of the new fraction
        if type(fraction) == 'Integer':
            fraction = Fraction(fraction)
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        result = Fraction(numerator, denominator)
        return result

    def __truediv__(self, fraction):
        """Defines the conventions for dividing a fraction by an integer or
           a fraction
           parameters:
           self - the fraction
           fraction - the divisor
           returns: 
           result - a new fraction that is the quotient of the two elements
        """
        if type(fraction) == 'Integer':
            fraction = Fraction(fraction)
        result = self * Fraction(fraction.denominator, fraction.numerator)
        return result
