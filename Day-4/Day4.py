import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# from the imported file `my_module`, we can call on that file with the variable/function within that file.
print(my_module.pi)


random_float = random.random()
print(random_float)

random_float_mult = random_float * 5
print(random_float_mult)
