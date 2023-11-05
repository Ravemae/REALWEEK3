# print(x)
# try: 
#     print(x)
# except IndexError:
#     print("The name is not defined")
# except:
#     print("An errr occurred")

# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only Integers are allowed")


fruits = ["apple", "banana"]

def make_drink(index):
    try: 
        fruit = fruits[index]
        print(fruit + " pie")
    except:
        print("An errr occurred")

make_drink(4)
