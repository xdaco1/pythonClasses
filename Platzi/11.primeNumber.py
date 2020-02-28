def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3,number):
            if number % i == 0:
                return False
            
        return True

def run():
    number = int(input("Write a number: "))
    result = isPrime(number)

    if result is True:
        print("The number is prime.")
    else:
        print("The number isn't prime.")

if __name__ == "__main__":
    run()