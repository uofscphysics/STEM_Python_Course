"""
DESCRIPTION:
    Graph an arbitrary function of 2 variables
    3d graph tends to be difficult to view because of angle
    2d heat map is likely to be a better choice


    Matplotlib Compatability:
        This function does not play nice with other graphs:
        Does not allow for graphing additional things on the same plot:
            fig = plt.figure() 
                Included in this method
            plt.draw() 
                Included in this method
        Can still be called amist other programs without a delay, because plt.show() is not invoked


ARGS (9 Count):
    Function:
        python function which has ARGS (1 count):
            Point:
                numpy array of two values
                point looks like [x_coord, y_coord]

        GraphTwoDimensionalDensityColorMap is designed to graph on 3 dimmensional coordinates
        Point == [x,y]
        F( Point )  => returns z

 
    DomainMinimumPoint:
        used for plot boundaries
        numpy array of two values:
            [x_min, y_min]

    DomainMaximumPoint:
        used for plot boundaries
        numpy array of two values:
            [x_max, y_max]

    ObservedDataset:
        Type_NumpyTwoDimensionalDataset
            [point, point, ...,  point]
        Used for scatter presentation

    PlotThreeDimensional:
        The plot generated will be a heat map regardless of choice with color correpsonding to density
        This can be two values:
            True
                Show visual third dimension and look at the surface from a fixed point
                Cannot plot contours
            False
                2D plot
                Will show contours

    Xlabel: ...
    Ylabel: ...
    Zlabel: ...


RETURNS:
    None

"""
import matplotlib.pyplot
import matplotlib
import matplotlib.pyplot as plt
import numpy
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#------------------------------------------------------------------------------

import Type_NumpyTwoDimensionalDataset
import Library_DatasetGetMinimumDatapoint
import Library_DatasetGetMaximumDatapoint


def Main( 
    Function = None, 
    DomainMinimumPoint = None, 
    DomainMaximumPoint = None, 
    ObservedDataset = None, 
    PlotThreeDimensional = False, 
    ShowContours = False, 
    PluginPointCount = None,
    Xlabel = "X", 
    Ylabel = "Y", 
    Zlabel = "Z",
    LogX = False,
    LogY = False, 
    CheckArguments = True,  
    SaveFigureFilePath = None,
    PrintExtra = False,
    ):
    
    if PluginPointCount is None:
        PluginPointCount = 10000
    PluginPointCountX = int(numpy.sqrt(PluginPointCount))
    PluginPointCountY = int(numpy.sqrt(PluginPointCount))

    if (CheckArguments): 
        ArgumentErrorMessage = ""
        #TODO: Match dataset and function dimensions

        if (Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True ):
            if (DomainMaximumPoint is None or DomainMinimumPoint is None ):
                ArgumentErrorMessage += "(Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True)\n"
                if (ObservedDataset is None):
                    ArgumentErrorMessage += "(ObservedDataset is None)\n"
                if (DomainMinimumPoint  is None):
                    ArgumentErrorMessage += "(DomainMinimumPoint  is None)\n"
                if (DomainMaximumPoint  is None):
                    ArgumentErrorMessage += "(DomainMaximumPoint  is None)\n"

        if (len(ArgumentErrorMessage) > 0 ):
            if (PrintExtra):
                print("ArgumentErrorMessage:\n", ArgumentErrorMessage)
            raise Exception(ArgumentErrorMessage)

    #Arg Fixing / Inferring (very pythonic - i know) 
    #Extract all the observations in X, Y coordinates:
    if (ObservedDataset is not None):
        ObservedX = ObservedDataset.T[0]
        ObservedY = ObservedDataset.T[1]
    else:
        ObservedX = numpy.array([])
        ObservedY = numpy.array([])

    #If a dataset was passed, and min/max plot domain not passed:
    #   infer the plot domain minimums and maximums from the dataset
    if (DomainMinimumPoint  is None):
        DomainMinimumPoint  = numpy.nanmin(ObservedDataset, axis = 0)
    if (DomainMaximumPoint  is None):
        DomainMaximumPoint  = numpy.nanmax(ObservedDataset, axis = 0) 

    print('DomainMinimumPoint', DomainMinimumPoint)
    print('DomainMaximumPoint', DomainMaximumPoint)

    xrng = DomainMaximumPoint [0] - DomainMinimumPoint [0]
    xmin = DomainMinimumPoint [0] #- xrng*0.2
    xmax = DomainMaximumPoint [0] #+ xrng*0.2    

    yrng = DomainMaximumPoint [1] - DomainMinimumPoint [1]
    ymin = DomainMinimumPoint [1] #- yrng*0.2
    ymax = DomainMaximumPoint [1] #+ yrng*0.2

    #Using the minimum and maximum points, we create a meshgrid of points
    #   This grid of points will be plugged into the function
    X, Y = numpy.mgrid[xmin:xmax:complex(PluginPointCountX), ymin:ymax:complex(PluginPointCountY)] #1000 x 1000 -> 1 million points
    PointsToPlugIn = numpy.vstack([X.ravel(), Y.ravel()])
    PointsToPlugInDataset = PointsToPlugIn.T
    PlugInPointsCount = len(PointsToPlugInDataset)

    print('PlugInPointsCount', PlugInPointsCount)
    print('PointsToPlugInDataset.shape', PointsToPlugInDataset.shape)
    print('PointsToPlugInDataset[0]', PointsToPlugInDataset[0])

    #Plug in each point into the function which is contained in the meshgrid
    #   Keep track of the values, and store them as "Z" coordinates
    FunctionResultValuesForGrid = []
    MaxObservedValue = None
    MinObservedValue = None
    for PointToPlugIn in PointsToPlugInDataset:
        FunctionValueForPointToPlugIn = None
        try:
            FunctionValueForPointToPlugIn = Function(PointToPlugIn)
            if numpy.isinf( FunctionValueForPointToPlugIn ) : 
                if FunctionValueForPointToPlugIn < 0:
                    FunctionValueForPointToPlugIn = 'MinMarker'
                elif FunctionValueForPointToPlugIn > 0:
                    FunctionValueForPointToPlugIn = 'MaxMarker'
            elif not numpy.isnan( FunctionValueForPointToPlugIn ):
                if MaxObservedValue is None or MaxObservedValue < FunctionValueForPointToPlugIn:
                    MaxObservedValue = FunctionValueForPointToPlugIn
                if MinObservedValue is None or MinObservedValue > FunctionValueForPointToPlugIn:
                    MinObservedValue = FunctionValueForPointToPlugIn

        except:
            print('Function(' , PointToPlugIn, ')', ' failed... skipping')
        FunctionResultValuesForGrid.append( FunctionValueForPointToPlugIn )

    print('MaxObservedValue', MaxObservedValue)
    print('MinObservedValue', MinObservedValue)
    FunctionResultValuesForGrid = [MaxObservedValue if item=='MaxMarker' else item for item in FunctionResultValuesForGrid ]
    FunctionResultValuesForGrid = [MinObservedValue if item=='MinMarker' else item for item in FunctionResultValuesForGrid ]
    #print 'FunctionResultValuesForGrid', FunctionResultValuesForGrid
    FunctionResultValuesForGrid = numpy.array(FunctionResultValuesForGrid)

    Z = numpy.reshape(FunctionResultValuesForGrid, X.shape)

    print('Z.shape', Z.shape)

    #print 'Z', Z

    #Plug in the observed points to get thier Z-values:
    if (ObservedDataset is not None):
        k = 0 
        ObservedPointsCount = len(ObservedDataset)
        ObservedZ = numpy.zeros((ObservedPointsCount))
        while (k < ObservedPointsCount ):
            PointToPlugIn = ObservedDataset[k]

            FunctionValueForPointToPlugIn = None
            try:
                FunctionValueForPointToPlugIn = Function(PointToPlugIn)
                print('FunctionValueForPointToPlugIn', FunctionValueForPointToPlugIn)
                #NumberGood = numpy.isfinite( FunctionValueForPointToPlugIn ) and not numpy.isnan( FunctionValueForPointToPlugIn )
            except:
                print('Function(' , PointToPlugIn, ')', ' failed... skipping')
                FunctionValueForPointToPlugIn = 0.0

            ObservedZ[k] = FunctionValueForPointToPlugIn
            k = k + 1


    zmin = numpy.min(Z) # This should always be 1 dimension
    zmax = numpy.max(Z) # This should always be 1 dimension
    zrange = zmax - zmin
    

    #size the graphs
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)

    fig = matplotlib.pyplot.figure(figsize=MonitorSize) #figsize=MonitorSize

    #matplotlib.pyplot.subplots_adjust(bottom=0.14)

    #Design the plot with the coordinate values (this could be done in it's own function)
    #fig = plt.figure()
    if (PlotThreeDimensional == True):
        subplot = fig.add_subplot(111, projection='3d')
        
        #Draw the mesh:
        surface = subplot.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.gist_earth_r) #cmap=cm.YlGnBu_r)
        fig.colorbar( surface )    

        #Draw a contour( This blows ):
        #contour = subplot.contour(X,Y,Z,extend3d=True )

        #Draw observations - veritical lines at each point (somehow this blows too):
        #k = 0
        #while k < ObservedPointsCount:
        #    subplot.plot( [ObservedX[k],ObservedX[k]],  [ObservedY[k], ObservedY[k]],  [ObservedZ[k] , ObservedZ[k] + zrange/20], 'w-', lw = 5 )
        #    k = k + 1
    
        #Draw observations - points in 3d (This blows ):
        #subplot.scatter(ObservedX, ObservedY, ObservedZ, marker= 'o', s=100, c = 'white')

        #ax.set_zlim3d(0, 1)
        subplot.set_xlabel(Xlabel)
        subplot.set_ylabel(Ylabel)
        subplot.set_zlabel(Zlabel)        

    else:

        #From http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html

        subplot = matplotlib.pyplot.subplot(111)
        #matplotlib.pyplot.subplot(2,1,2)


        #aspectratio = xrng / yrng
        aspectratio = 'auto'

        heatmap = subplot.imshow( 
        #heatmap = matplotlib.pyplot.imshow(
        #heatmap = matplotlib.pyplot.imshow(
            numpy.rot90(Z), 
            #cmap=plt.cm.gist_earth_r, 
            extent=[xmin, xmax, ymin, ymax] ,
            aspect = aspectratio ,
            interpolation = None,
            #norm=LogNorm(vmin=0.01, vmax=1)
            )  


        #Add color bar (showing Z-axis sense of scale)
        matplotlib.pyplot.colorbar( heatmap, label = Zlabel )

        #matplotlib.pyplot.tight_layout()

        #Add the observations:
        if (ObservedDataset is not None):
            matplotlib.pyplot.plot(ObservedX, ObservedY, 'k.', markersize=2)

        #Set image boundaries:
        #subplot.set_xlim([xmin, xmax])
        #subplot.set_ylim([ymin, ymax])
        subplot.set_xlabel(Xlabel)
        subplot.set_ylabel(Ylabel)
        #plt.axis([xmin, xmax, ymin, ymax])
        #matplotlib.pyplot.autoscale(axis='y')
        #heatmap.set_aspect(1)


        #subplot.set_xscale('log')


        #Plot Countours: ( From http://matplotlib.org/examples/pylab_examples/contour_demo.html )
        if( ShowContours ):
            CS = plt.contour(X, Y, Z, 6,
                             colors='k', # negative contours will be dashed by default
                             )

            plt.clabel(CS, fontsize=9, inline=1)

            plt.title("Density Map + Contours")
        else:
            plt.title("Density Map")



    if (SaveFigureFilePath is not None):
        plt.savefig( SaveFigureFilePath )

    plt.draw()





    """
    #Extract boundary regions (minimum and maximum points)
    if (DomainMinimumPoint  is None):

            DomainMinimumPoint  = Library_DatasetGetMinimumDatapoint.Main(ObservedDataset)
        else:
            #Better: We have to spotcheck infer where the Z axis ranges with monte-carlo
            raise Exception("DomainMinimumPoint not defined")
    if (DomainMaximumPoint  is None):
        if (ObservedDataset is not None):
            DomainMaximumPoint  = Library_DatasetGetMaximumDatapoint.Main(ObservedDataset)
        else:
            raise Exception("DomainMaximumPoint not defined")
    """

































