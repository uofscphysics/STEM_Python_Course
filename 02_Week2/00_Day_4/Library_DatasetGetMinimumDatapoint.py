"""
DESCRIPTION:
    Gets the minimum theoretical point of a domain box
    This is the same as taking a list of each maximum observed cartesian coordinate

ARGS:
    Dataset:
        Type: Type_NumpyTwoDimensionalDataset
            [
            [X1a, X2a, ... XNa]
            [X1b, X2b, ... XNb]
            [X1c, X2c, ... XNc]
            ]

RETURNS:
    MinPoint
        Type: `Type_NumpyTwoDimensionalDataPoint`
        Description: [ Min(X1's) , Min(X2's), ..., Min(XN's) ]
"""

import numpy

def Main(Dataset):
	DatasetTranspose = Dataset.T
	DatasetDimensionMinimums = []
	for DimensionValues in DatasetTranspose:
		DatasetDimensionMinimums.append(min(DimensionValues))
	Result = numpy.array(DatasetDimensionMinimums)
	return Result
