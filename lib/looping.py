def happy_new_year():
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i)
    print("Happy New Year!")  # Celebration message

def square_integers(int_list):
    return [x ** 2 for x in int_list]  # Use a list comprehension to square each element

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
