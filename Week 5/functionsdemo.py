#using zip() function
a=("John","Oliver","Malcolm","Barry")
b=("Doe","Queen","Merlin","Allen","XYZ")
x=zip(a,b)
print(tuple(x))

#using enumerate() function
l1=["eat","sleep","repeat"]
s1="geek"

#creating enumerate objects
obj1=enumerate(l1)
obj2=enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

#changing start index to 2 from 0
print(list(enumerate(s1,2)))

#lambda function - calc
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

#filter lambda
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101")

do_exclaim = lambda s: s + '!'
print()

find_sum lambda n: sum([int x 
print()

#function vs lambda
def cube(y):
    print()
    return y * y * y

lambda_cube = 

#invoking simple function

print(cube(30))
#invoking lambda function


#
l = {"1","2"}


#
mewlist = list(filter(lambda x: x % 2 