import numpy
#------------------------------------------------------------------------------
import Type_NumpyTwoDimensionalDataset
import Library_PrintFullTestSuccess
import Library_PrintNumpyArrayInfo

FullTestSuccess = True #Assume inocent until proven guilty

###############################################################################
#GOOD FORMS:

GoodData1   = numpy.array(  [[1,2]] )                       #1 point dataset (2dim)
GoodData2   = numpy.array(  [[1,2],     [3,4]] )            #2 point dataset (2dim) 
GoodData3   = numpy.array(  [[1,2,3],   [4,5,6]]  )         #2 point dataset (3dim)
GoodData4   = numpy.array(  [[1,2],     [3,4],  [5,6]] )    #3 point dataset (2dim)

GoodDatasetList = [GoodData1, GoodData2, GoodData3, GoodData4]

###############################################################################
#BAD FORMS:

#   Datapoints which are different number of dimensions
#       Omited coordinate could be mathematically treated as every possible value 
#       This would be arguous task to make work, so we will mark data of this form as BAD
BadData1 = numpy.array(     [[1,2,3], [4,5]] )

#   Tensor which is not projected onto a 2 dimensional code dataset
#       (this is 3 Dim code data -> 2x2x2,  and this is not handled by any code. 
#       these same coordinates could be projected into a 2 dimensional code tensor, 
#       of the form:  [ point1 == [x,y,z] , [point2], ... , [point8] ]
#       But that is out of the scope of the work that is logical
BadData2 = numpy.array(     [[[1,2], [3,4]],[[7,8], [10,11]]] )
BadData3 = numpy.array(     [[[[1,2], [3,4]],[[5,6], [7,8]]],[[[11,12], [13,14]],[[15,16], [17,18]]]] )
BadDatasetList = [BadData1, BadData2, BadData3]



for Dataset in GoodDatasetList:
    if ( Type_NumpyTwoDimensionalDataset.Main(Dataset = Dataset) ):
        print("Dataset Check Sucess")
    else:
        print(" Dataset Check Failure. \n")
        Library_PrintNumpyArrayInfo.Main(Dataset)
        FullTestSuccess = False #Mark that at least one test has failed

for Dataset in BadDatasetList:
    if ( Type_NumpyTwoDimensionalDataset.Main(Dataset = Dataset) == False):
        print("Dataset Check Sucess")
    else:
        print(" Dataset Check Failure. \n")
        Library_PrintNumpyArrayInfo.Main(Dataset)
        FullTestSuccess = False #Mark that at least one test has failed



Library_PrintFullTestSuccess.Main(FullTestSuccess)












