# dec.py

"""
0. run python file in terminal, open as environment
1. use dis to get information about function
2. look at byte code for function
3. look at default arguments for function
4. look at name of function

"""

#%%
# foo is a decorator which will add ', fucking.' to the sentence created by bar.
# bar is a function that will return "Hi, my name is x".
def foo(fn):
    def f(*args, **kwargs):
        return fn(*args, **kwargs) + ", fucking."
    return f


@foo
def bar(x):
    return "Hi, my name is {}".format(x)

@foo
def biff(x):
    return str(x)

def print_goals():
    print("""
    0. run python file in terminal, open as environment
    1. use dis to get information about function
    2. look at byte code for function
    3. look at default arguments for function
    4. look at name of function

        """)

print(bar("Alex"))
print(biff(31))
print_goals()

#%%
