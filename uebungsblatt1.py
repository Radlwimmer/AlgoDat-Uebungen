#exercise 1

def name_age():
    name = input("Please state your name: ")
    age = input("Please state your age: ")

    print(f"Hello {name}! Your age is: {age}")


#exercise 2

def swap_integers():
    x = input("Please enter NUmber X: ")
    y = input("Please enter NUmber Y: ")

    print(f"X={x}")
    print(f"Y={y}")
    x,y = y,x
    print("After swap:")
    print(f"X={x}")
    print(f"Y={y}")


#exercise 3

def check_numbers(num1:int,num2:int):
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    if num1 % 6 == 0 or num2 % 6 == 0:
        print("One number is divisible by 6")
    else:
        print("One number is not divisible by 6")
    if num1 % 10 == 0 and num2 % 10 == 0:
        print("Both numbers are divisible by 10")
    else:
        print("At least one number is not divisible by 10")
    if (num1 % 6 == 0 or num2 % 6 == 0) and num1 % 10 == 0 and num2 % 10 == 0:
        return True
    else:
        return False



#exercise 4

def sum_up(num1:int,num2:int):
    if num1 >= num2:
        print("Second number must be greater than first number")
        return
    else:
        sum = 0
        while num1 <= num2:
            sum += num1
            num1 += 1

        return sum


#exercise 5

def sequence(num:int):

    if num < 0 or num > 9:
        print("Number must be between 0 and 9")
        return
    else:
        for i in range(10):
            if i != num:
                print(i, end=" ")



#exercise 6

def check_string(text:str):
    text = str.casefold(text)
    if str.endswith(text, "a") or str.startswith(text, "a"):
        return True
    else:
        return False


#exercise 7

def triangle(rows:int):
    if rows < 1:
        print("There has to be at least one row.")
    else:
        for i in range(rows):
            for j in range(i+1):
                if j == i:
                    print("*")
                else:
                    print("*", end=" ")

