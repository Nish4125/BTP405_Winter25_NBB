def processNumberDecorator(func):
    def wrapper(numbers):
       print(f"Numbers: {numbers}")      
       print(f"Count Of Numbers: {len(numbers)}")
       print(f"Sum of Numbers: {sum(numbers)}")
       return func(numbers)
    return wrapper

@processNumberDecorator
def processNumber(numbers):
    print("Processing the numbers...")

numberList = [5, 10, 20, 23, 50]
processNumber(numberList)



