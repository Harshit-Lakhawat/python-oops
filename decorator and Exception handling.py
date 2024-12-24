def add_sprinkles(function):
    def wrapper(*args,**kwargs):
        print("you add sprinkles")
        function(*args,**kwargs)
    return wrapper

def add_fudge(function):
    def wrapper(*args,**kwargs):
        print("you add fudge")
        function(*args,**kwargs)
    return wrapper
@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream ")

get_ice_cream("vanilla")



# Exception handling
try:
    number = int(input("enter a number : "))
    print(1/number)

except ZeroDivisionError:
    print("You cannot divide a number by zero idiot")

except ValueError:
    print("Are you mad you are asked to put number")

except Exception: #bad practice only use this if you are unable to know what went wrong
    print("something went wrong")

finally: #this block always execute whether there is exception or not
    print("Do some cleanup here")
