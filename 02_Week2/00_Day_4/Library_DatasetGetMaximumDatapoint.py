"""
DESCRIPTION:
    Gets the maximum theoretical point of a domain box
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
    MaxPoint
        Type: `Type_NumpyTwoDimensionalDataPoint`
        Description: [ Max(X1's) , Max(X2's), ..., Max(XN's) ]
"""

import numpy
def Main(Dataset = None):
	DatasetTranspose = Dataset.T
	DatasetDimensionMinimums = []
	for DimensionValues in DatasetTranspose:
		DatasetDimensionMinimums.append(max(DimensionValues))
	Result = numpy.array(DatasetDimensionMinimums)
	return Result
