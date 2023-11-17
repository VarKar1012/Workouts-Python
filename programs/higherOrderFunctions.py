# first class functions

# def sqr(x): return x*x

# var = sqr
# print(var(3))
# --------------------------------------------

# higher order function: a function is passed as argument to another function

# def sqr(x): return x*x

# def mymap(func, var):
#     l = []
#     for i in var:
#         l.append(func(i))
#     return l

# res = mymap(sqr, [1,3,4,5])
# print(res)
# --------------------------------------------
# closures

# def outerFn(val):
#     msg = 'hi'
#     def innerFn():
#         print(msg, val)
#     return innerFn

# var = outerFn('world')
# var()
# # hi world
# ////////////////////////////////////////
# def html_tag(tag):
#     def display(msg):
#         print(f"<{tag}>{msg}</{tag}>")
#     return display

# v = html_tag('h1')
# v('hello world')
# <h1>hello world</h1>
# -------------------------------

# Wrapper function - DEcorator function

# def decoratorFunc(orgFunc):
#     def wrapperFunc():
#         print(f"wrapper executed before {orgFunc.__name__}")
#         return orgFunc()
#     return wrapperFunc

# def display():
#     print("inside display function")

# wrapped = decoratorFunc(display)
# wrapped()
# output:
# wrapper executed before display
# inside display function
# ////////////////////////////////////
# using decorators
# def decoratorFunc(orgFunc):
#     def wrapperFunc():
#         print(f"wrapper executed before {orgFunc.__name__}")
#         return orgFunc()
#     return wrapperFunc

# @decoratorFunc
# def display():
#     print("inside display function")

# display()
# output:
# wrapper executed before display
# inside display function
# //////////////////////////////////////
# def decoratorFunc(orgFunc):
#     def wrapperFunc(name, age):
#         print(f"wrapper executed before {orgFunc.__name__}")
#         return orgFunc(name, age)
#     return wrapperFunc

# @decoratorFunc
# def displayInfo(name, age):
#     print(f"display_info with args: {name} & {age}")

# displayInfo('Devin', 28)
# out:
# wrapper executed before displayInfo
# display_info with args: Devin & 28
# ////////////////////////////////////////
def decoratorFunc(orgFunc):
    def wrapperFunc(*args, **kargs):
        print(f"wrapper executed before {orgFunc.__name__}")
        return orgFunc(*args, **kargs)
    return wrapperFunc

@decoratorFunc
def displayInfo(name, age):
    print(f"display_info with args: {name} & {age}")

displayInfo('Devin', 28)
# out: 
# wrapper executed before displayInfo
# display_info with args: Devin & 28