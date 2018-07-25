# Topic: first-class object


# In python, function is object !
def yell(text):
    return text.upper() + '!'
print(yell('hello'))

# Object can be assigned to another variable
bark = yell
print(bark('woof'))

# you can delete function name
# def yell
# Show insight identificative word by .__name__
print("obj.__name__ : ", bark.__name__)


# function can be putting into a data structure
funcs = [bark, str.lower, str.capitalize] # putting into a list
print(funcs)

for f in funcs:
    print(f, " :",f('hey there'))


#-----------------------------
print("\n higher-order function::")
print("\nbark into greet function :" )
def greet(func):
    greeting = func("Hi, I am a Python program ！")
    print(greeting)
greet(bark)

print("\nwhisper into greet function :")
def whisper(text):
    return text.lower() + "..."
greet(whisper)

print("\nhigher-order function example: map()")
print(
      list( map(bark, ['Hello', 'hey', 'big big']) )
     )


#-----------------
print("\nnested (inner) function::")
# for example
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)
print(speak('Hello World!'))


print("\n inner function return to outside: ")
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."
    def yell(text):
        return text.upper() + "..."
    if volume > 0.5:
        return yell
    else:
        return whisper

wh_f = get_speak_func(0.7)
ye_f = get_speak_func(0.3)
print(wh_f("Hello!"),"\n", ye_f("Hello!"))


#-----------------------------------------
print("\n inner func. can capture parts of outside func. ::")

def get_speak_func_2(text, volume):
    def whisper():
        return text.lower() + "...."
    def yell():
        return text.upper() + "...."
    if volume > 0.5:
        return yell
    else:
        return whisper

print(
      get_speak_func_2('Hello!', 0.7)()
     )


#--------------
print("\n Function factory::")

def adder(n):
    def add(x):
        return x + n
    return add

plus_3 = adder(3)
plus_6 = adder(6)

print(plus_3(5), "\n", plus_6(5))


#----------------------------
print("\n Callable and __call__ ::")

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(Adder(3), plus_3(4))

print("\ncallable function:")
print(callable(plus_3))
