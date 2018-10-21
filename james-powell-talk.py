# dec.py

"""
0. run python file in console, open as environment
1. use dis to get information about method
2. look at byte code for method
3. look at default arguments for method
4. look at name of method

"""

# %%
# foo is a decorator which will add ', heckin.' to the sentence created by bar.
# bar is a method that will return "Hi, my name is x".


def foo(func):
    def f(*args, **kwargs):
        return func(*args, **kwargs) + ", heckin."
    return f


@foo
def bar(x):
    return "Hi, my name is {}".format(x)


@foo
def biff(x):
    return str(x)


def print_goals():
    print("""
    0. run python file in console, open as environment
    1. use dis to get information about method. This will tell you the exact stuff that the method is doing.
    2. look at byte code for method
    3. look at default arguments for method
    4. look at name of method

        """)

#%%
def testing_out_syntax(num1: int, num2: int, st: str) -> str:
   return str('num1 + num2 = {} '.format(num1 + num2) + ', and the string is {}'.format(st))
   
print(testing_out_syntax(1, 2, 5))