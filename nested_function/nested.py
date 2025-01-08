##Example 1

""" def outer(x):

    def inner(y):
        return x+y 
      
    return inner(5)
    

print(outer(6)) """

##Example 2

def outer(x):

    def inner(y):
        return x + y
    
    return inner

print(outer(5)(6))
''' 
In Python, closures allow a nested function to remember the state of its enclosing scope when it is called.

1. `outer(5)` sets `x=5` and returns the `inner` function.
2. When `inner(6)` is called, it uses the value of `x` from the enclosing scope of `outer`, which is `5`.
3. The `inner` function then performs the operation `x + 6`.
'''