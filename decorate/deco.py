#the sample code is referred from 
#https://foofish.net/python-decorator.html

def logging(inStr):
    print(inStr)

def user_logging(func):
    logging("%s is running" % func.__name__)
    func()

#Modify user_logging to for step 2
def user_logging1(func):
    def wrapper():
        logging("%s is running" % func.__name__)
        return func()
    return wrapper

#Modify user_logging to for step 4
def user_logging2(func):
    def wrapper(name):
        logging("%s is running" % func.__name__)
        return func(name)
    return wrapper

#Modify user_logging to for step 5
def user_logging3(func):
    def wrapper(*args):
        logging("%s is running" % func.__name__)
        return func(*args)
    return wrapper

def foo():
    print('i am foo')

#code for step 3
@user_logging1
def fan():
    print("I am fan")

#code for step4 , wang() with one input parameter
@user_logging2
def wang(strName):
    print("I am %s"%strName)

#code for step5 ,  with multi- input parameters
@user_logging3
def ying(strName, age=None, height=None):
    print("I am %s. age = %d, height = %d"%(strName, age, height))    

#Mark this for step 2
# user_logging(foo)              

#code for step 2
foo = user_logging1(foo)     # foo = wrapper
foo()

#code for step 3
fan()

#code for step 4
wang("wang1")
#code for step 5
ying("louis", 50, 175)