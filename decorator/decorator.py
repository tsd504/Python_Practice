def make_pretty(func):

    def inner():

        print("I got decorated")

        func()

    return inner

def ordinary():
    print("I am ordinary")
    
decorated_func = make_pretty(ordinary)()

'''
The make_pretty(ordinary) call sets the function to ordinary
the make_pretty function returns inner which then calls inner()
then the two lines are printed.
'''