"""
DESCRIPTION:
    Prints some useful informatoin about a numpy array 
    includes things like:
        shape
        type
        the values
        ...

ARGS (1 Count):
    Dataset -> any numpy.array

RETURNS (0 count):
    None

TESTS:
"""
def Main(Dataset = None):
    print(" Dataset: \n" , Dataset)
    print(" Dataset.shape: \n", Dataset.shape)
    print(" type(dataset): \n", type(Dataset))
