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
