
def FizzBuzzStringConstruct( MaximumNumber = None ) :

    for num in range(1,MaximumNumber):
        string = ""
        if num % 3 == 0:
            string = string + "Fizz"
        if num % 5 == 0:
            string = string + "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            string = string + str(num)
        print(string)

    return string


ExampleMaximumNumber = 21
FizzBuzzStringConstruct ( 
    MaximumNumber = ExampleMaximumNumber,
    )
