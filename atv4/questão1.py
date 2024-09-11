for contador in range(1,51):
    if contador % 3 == 0:
        print("Fizz")
    
    if contador % 5 == 0:
        print("Buzz")

    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    
    else:
        print(contador)