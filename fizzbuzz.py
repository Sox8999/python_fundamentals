def fizzbuzz():
    # loop from 0 to 100
    for i in range(101):
        #as we loop, check if number is evenly divisible by 3
        if i % 3 == 0 and i % 5 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i


fizzbuzz()
