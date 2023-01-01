import numpy as np

#bad example
def math_operations(list_):
    # Compute Average
    print(f"the mean is {np.mean(list_)}")
    # Compute Max
    print(f"the max is {np.max(list_)}")



#　Correct example
def get_main(list_):
    print(f"the mean is ({np.mean(list_)}")

def get_max(list_):
    print(f"the max is {np.max(list_)}")