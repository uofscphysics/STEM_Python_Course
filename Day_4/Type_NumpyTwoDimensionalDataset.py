
"""
Type_NumpyTwoDimensionalDataset

Desciption:

    Checks to see if the only arg `Dataset` is of the following form:
        Dataset
        == 
        [point, point, ... , point]
        ==
        [ 
        [point1_x1,point1_x2,..,point1_xN], 
        [point2_x1,point2_x2,..,point2_xN], 
        .
        .
        .,
        [pointK_x1,pointK_x2,..,pointK_xN], 
        ]

ARGS:
    Dataset: (any) 
        This is the thing we are checking

    PrintExtra: (boolean)

RETURNS:
    True -> when dataset meets criterion for `Type_NumpyTwoDimensionalDataset`

    OR
    
    False -> when dataset does NOT meet criterion for `Type_NumpyTwoDimensionalDataset`


"""

import numpy
#------------------------------------------------------------------------------

def Main(
    Dataset = None, 
    PrintExtra = False
    ):

    #Must not be null
    if Dataset is None:
        if (PrintExtra):
            print("Emtpy Dataset: Must not be null")
        return False 

    #Type Numpy Array
    if ( str(type(Dataset)) != "<type 'numpy.ndarray'>" ):
        if (PrintExtra):
            print("DatasetType:  must be Type Numpy Array")
        return False
    
    #Must be Two Code Dimensions (even for N-Dimensional Datasets)
    if (len(Dataset.shape) != 2):
        if (PrintExtra):
            print("len(Dataset.shape) != 2: Must be Two Code Dimensions (even for N-Dimensional Datasets)")
        return False

    #For N-Dimensional datasets - they must be at least 1 dimension
    if (Dataset.shape[0] < 1): 
        if (PrintExtra):
            print("DatasetShape[0] < 1:  For N-Dimensional datasets - they must be at least 1 dimension")
        return False

    #For N-Dimensional datasets - they must have at least 1 observation
    if (Dataset.shape[1] < 1):
        if (PrintExtra):
            print("DatasetShape[1] < 1 For N-Dimensional datasets - they must have at least 1 observation")
        return False
        
    return True
    
