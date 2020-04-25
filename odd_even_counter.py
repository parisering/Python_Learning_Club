
my_tuple = (1,2,3,4,5)

def even_odd_counter(numbers):
    for number in numbers:
        if number % 2 == 0:
            print("EVEN")
        else:
            print("ODD")

even_odd_counter(my_tuple)