#This function protect the function protected_func
def protect_access(func):
    def wrapper(pswd):
        if pswd == 'platzi':
            return func()
        else:
            print('Access not granted!')
    
    return wrapper

# Protected function (behavior) by a password
@protect_access
def protected_func():
    print('Access Granted!')

if __name__ == "__main__":
    password = str(input('Write your password: '))

    protected_func(password)