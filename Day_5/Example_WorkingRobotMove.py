
import numpy

#w -> up
#s -> down
#a -> left
#d -> right

def MoveRobotBasedOnMovementString( 
    StartPosition = None,
    MovementString = None,
    ):


    Position = numpy.array( StartPosition )
    for Char in ExampleMovementString:
        if Char is 'w': Position = Position + numpy.array([0,1])
        elif Char is 's': Position = Position + numpy.array([0,-1])
        elif Char is 'a': Position = Position + numpy.array([1,0])
        elif Char is 'd': Position = Position + numpy.array([-1,0])            
        else:
            raise Exception( 'unrecognized character' )    

    FinalPosition = Position
    return FinalPosition


ExampleMovementString = 'wasdwsdwadwasdssssddddwwwwwsswwdasdwadaaadsdwdwdwdwdwdwd'
ExampleStartPosition = [1,1]



FinalPosition = MoveRobotBasedOnMovementString(
    StartPosition  = ExampleStartPosition ,
    MovementString = ExampleMovementString,

    )


print ('FinalPosition', FinalPosition)
