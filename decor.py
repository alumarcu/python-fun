#
# Functions as decorators
#
# Tutorials from:
# http://www.artima.com/weblogs/viewpost.jsp?thread=240808
# http://www.artima.com/weblogs/viewpost.jsp?thread=240845
##
def wrap_decor(user_func):
    def wrapped_func(): # No need to pass the function as argument
        print "Hacking into a user supplied function: %s" % user_func.__name__
        raw = user_func()
        message = ''
        if isinstance(raw, str):
            message = raw.lower() + " was h4xx0r3d!"
        print "Finished hacking user supplied function: %s" % user_func.__name__
        return message
    return wrapped_func # The decorator function must be returned!

@wrap_decor
def naive_hello():
    return "Hello World"
    
#
# Classes as decorators
##

class BurgerDecorator(object): 
# A base decorator so that other ingredients can be done easier
    
    _the_ingredient = "" 

    def __init__(self, burger_func):
        # Stuff here gets executed in the beginning of execution
        # when a function uses the decorator
        print "__init__ Initializing ingredient: %s" % self.__class__.__name__
        self._burger = burger_func # Which is why we save the callback
        
    def __call__(self): # Arguments for the decorator
        # Here hack the function so we can add stuff to the burger!!
        print "__call__ Customer wants: %s" % self.__class__.__name__
        bur = self._burger()
        bur = bur.replace(" nothing",":") # Something was added to the burger!
        if isinstance(bur, str):
            bur += " " + self._the_ingredient + "," # Add the salad
        return bur            

class BurgerSpiceDecorator(object):
# These decorators will contain an argument
    _the_ingredient = ""
    _qty = None

    def __init__(self, qty):
        # qty: how much of the ingredient is included
        print "__init__ Getting ingredient specs: %s"  % self.__class__.__name__
        self._qty = qty # Set the ingredient as property
        
    def __call__(self, burger_func):
        # Note that the burger_func is supplied here instead
        print "__call__ Creating ingredient after specs: %s"  % self.__class__.__name__
        def new_recipe(*args): # args would be used if get_burger would have args
            # Hack the function and add the ingredient here
            bur = burger_func()  # Note that I'm running the function here!
            bur = bur.replace(" nothing",":") # Something was added to the burger!
            if isinstance(bur, str):
                bur += " " + "%s kg of " % self._qty + self._the_ingredient + "," # Add the salad
            return bur
        # Send the new recipe here
        return new_recipe

# Raw Ingredients
class freshSalad(BurgerDecorator):
    _the_ingredient = "fresh crispy green salad"
class sourPickles(BurgerDecorator):
    _the_ingredient = "sour yummy pickles"
# Spices with quantity
class ketchup(BurgerSpiceDecorator):
    _the_ingredient = "ketchup"
class salt(BurgerSpiceDecorator):
    _the_ingredient = "salt"

@ketchup(2)
@salt(0.22)
@freshSalad
@sourPickles
def get_burger():
    return "You get a burger with nothing"


