# function named hello that prints a greeting 

def hello():
    print("hello")

#function named pack that accepts three arguments, and returns a single list with the arguments

def pack(one, two, three):
    return [one, two, three]

# function named eat_lunch that accepts a list of any length, and prints out a series of strings that say
# "first i eat __", and "next i eat__". if the list is empty, print "my lunchbox is empty"
#do not return anything with this function.

def eat_lunch(list):
    if len(list) == 0:
        print("my lunchbox is empty")
    else:
      for lunch in range(len(list)):
        if lunch == 0:
          print(f"first I eat {list[0]}")    
        else:
          print(f"next i eat {list[lunch]}")    


#test 

hello()

print(pack("one","two","three"))
print(pack(1,2,3))

eat_lunch([])
eat_lunch(["steak"])
eat_lunch(["salad","fruit","chocolate"])