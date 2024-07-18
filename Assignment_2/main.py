from math import sqrt

def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def subtraction(*args):
    result = args[0]
    for arg in args[1:]:
        result -= arg
    return result

def multiplication(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def division(numerator, denominator):
    quotient = numerator / denominator
    remainder = numerator % denominator
    return (quotient, remainder)

def exponential(base, exponent):
    return base ** exponent

def square_root(num):
    return sqrt(num)

def default_case():
    return "Invalid choice"

def switch_case(argument, *args):
    switcher = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: exponential,
        6: square_root,
    }
    func = switcher.get(argument, default_case)
    return func(*args)


def main():
    print('This a calculator function')
    print('This can provide following operations:')
    print('1:Addition')
    print('2:Subtraction')
    print('3:Multiplication')
    print('4:Division')
    print('5:Exponential')
    print('6:sqaure_root')
   
    option = int(input('Enter the choice of operation (1-6): '))
    
    if option in (1, 2, 3, 5):
        nums = list(map(float, input('Enter the numbers separated by space: ').split()))
    elif option == 4:
        numerator = float(input('Enter the numerator: '))
        denominator = float(input('Enter the denominator: '))
        nums = (numerator, denominator)
    elif option == 6:
        num = float(input('Enter the number for square root: '))
        nums = (num,)
    else:
        print('Invalid choice')
        return
    
    result = switch_case(option, *nums)
    print(f'Result: {result}')

if __name__ == "__main__":
    main() 
