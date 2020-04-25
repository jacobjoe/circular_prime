# import time module for calculating the speed of operation takes place
from time import time
start = time()


# define a class
class CircularPrime:
    # define a method and pass parameters
    def find_circular_prime(self, first, last):
        # while loop for loop between the given first and last number
        while first <= last + 1:
            # string_1 for circular action
            string_1 = str(first)
            # string_2 for comparing the circulated string to initial string and stop circulation
            string_2 = str(first)
            # list_1 for append circular strings
            lst_1 = []
            # list_2 for append strings of prime values
            lst_2 = []
            # while True used for loop inside until the break operation takes place
            while True:
                string_1 = string_1[1:] + string_1[0]
                lst_1.append(string_1)
                if string_2 == string_1:
                    break
            # for loop for take the first string(circular) in the list
            for j in lst_1:
                k = int(j)
                # nested for loop for check the value whether it is prime or not
                for m in range(2, k):
                    if k % m == 0:
                        break
                else:
                    lst_2.append(j)
            # if condition for check the list_1 (circular strings) and list_2(prime strings)
            if lst_1 == lst_2:
                print(first)
            first += 1


# create an object for the class
c_prime = CircularPrime()
# call the method by using created object and pass the argument
c_prime.find_circular_prime(2, 10000)
end = time()
# print statement for print the calculated time
print(f'Time :{end - start} seconds.')
