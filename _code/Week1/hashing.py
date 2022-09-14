import timeit
import random


# Build a class that will hash objects badly
class BadHashObj():

    def __init__(self, my_val):
        # This class has one member variable,
        # so we have something to hash
        self.value = my_val

    def __hash__(self):
        # This hash function can only ever return 
        # 1 or 0
        return self.value % 2


# Build a class that will hash objects well
class GoodHashObj():

    def __init__(self, my_val):
        # Set up class the same as the other,
        # for a controlled comparison
        self.value = my_val

    def __hash__(self):
        # Using Python's built-in hash function on
        # self.value should be pretty good
        return hash(self.value)


# A function that tries out using the bad hash object
def use_bad_hash_obj():
    # Checking whether an integer is in the global bad_hash_dict
    # hash-table will force us to use BadHashObj's hash function
    BadHashObj(random.randint(1, 1000)) in bad_hash_dict


# A function that tries out using the good hash object
def use_good_hash_obj():
    # Do the same thing as the test of the bad  hash object
    GoodHashObj(random.randint(1, 1000)) in good_hash_dict


# Print a header label 
print("n, good, bad")

# Test the effect at n of various orders of magnitude
for n in range(0, 100000, 10000):

    # Populate bad_hash_dict and good_hash_dict
    bad_hash_dict = {}
    for i in range(n):
        bad_hash_dict[BadHashObj(random.randint(1, 1000))] = 1

    good_hash_dict = {}
    for i in range(n):
        good_hash_dict[GoodHashObj(random.randint(1, 1000))] = 1

    # Now we can actually measure the time impact of using
    # a bad hash function vs. a good one
    bad_time = timeit.timeit(use_bad_hash_obj, number=1000)
    good_time = timeit.timeit(use_good_hash_obj, number=1000)
    print(",".join([str(n), str(good_time), str(bad_time)]))
