#  File: Goldbach.py

#  Description: inputs a range of numbers and outputs all the sums of prime numbers in the even numbers of that range according to the Goldbach's Conjecture

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 02/22

#  Date Last Modified: 02/26

def main():

    def is_prime(n):
        if n == 1:
            return False

        if n == 2:
            return True

        divisor = 2
        limit = int(n**0.5) + 1

        while  (divisor<limit) :

            if n%divisor == 0 :

                return False

            divisor += 1

        return True

        
    lower = eval(input("Enter lower limit: "))
    upper = eval(input("Enter upper limit: "))
    

    while lower<4 or upper<=lower or (upper%2!=0) or (lower%2!=0) :

        lower = eval(input("Enter lower limit: "))
        upper = eval(input("Enter upper limit: "))
        

    counter = lower

    first = 2

    second = 0

    

    while counter <= upper:

        print( str(counter), end = "")

        while first <= (counter/2) :

            if is_prime(first):


                second = counter - first

                if is_prime(second):

                    print( " = " + str(first) + " + " + str(second), end = "")

                    first += 1

                else :

                    first += 1

            else:
                first += 1


        counter += 2

        first = 2

        print()







main()
