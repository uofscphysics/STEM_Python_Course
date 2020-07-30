
SUBROUTINE wave_propogation_fortran(num_steps, scale, damping, initial_P, stop_step, P)
  ! INPUTS
  ! num_steps -> int # Number of itereations to make
  ! scale -> int # Size of box for wave to propogate in
  ! damping -> float # Factor for damping wave
  ! initial_P -> float # Initial height at center
  ! stop_step -> int # Number of steps to stop wave
  ! OUTPUTS:
  ! P -> float(x,y) # Array of output heights
  IMPLICIT NONE
  INTEGER size_x,i,j,k,step
  REAL PI, omega
  INTEGER, INTENT(in)  :: num_steps, scale, stop_step !input
  REAL, INTENT(in) :: damping, initial_P !input
  REAL, INTENT(out) :: P(2 * scale + 1,2 * scale + 1) ! output
  REAL, DIMENSION(2 * scale + 1,2 * scale + 1,4) :: V

  size_x = 2 * scale + 1

  PI = 3.14159
  omega = 3.0 / (2.0 * PI)

! Setup initial matrix all 0's
! P is pressure matrix
! V is velocity tensor (matrix of x/y and 4 vector of velocity [up,down,left,right])
  DO k=1,4
     DO j=1,size_x
        DO i=1,size_x
           P(i,j) = 0.0
           V(i,j,k) = 0.0
        END DO
     END DO
  END DO

  ! Set initial start height
  P(scale + 1,scale + 1) = initial_P

  ! For each step
  DO step = 1, num_steps
    ! If step is less than stopping step then add forcing function
    IF(step <= stop_step) THEN
      P(scale + 1 ,scale + 1) = initial_P * SIN(omega * step)
    ENDIF

    ! For each cell in matrix P
    DO j=1,size_x
      DO i=1,size_x
        IF (i == 0) THEN
          CYCLE
        END IF
        ! Calculate veolocity of wave at the points
        V(i,j,1) = MERGE(V(i,j,1) + P(i,j) - P(i - 1,j), P(i,j), i > 1)
        V(i,j,2) = MERGE(V(i,j,2) + P(i,j) - P(i,j + 1), P(i,j), j < size_x - 1)
        V(i,j,3) = MERGE(V(i,j,3) + P(i,j) - P(i + 1,j), P(i,j), i < size_x - 1)
        V(i,j,4) = MERGE(V(i,j,4) + P(i,j) - P(i,j - 1), P(i,j), j > 1)
      END DO
    END DO

    DO j=1,size_x
      DO i=1,size_x
        ! Get new pressure from P = P_0 - damping*V
        P(i,j) = P(i,j) - 0.5 * damping * (V(i,j,1) + V(i,j,2) + V(i,j,3) + V(i,j,4))
      END DO
    END DO
  END DO

END SUBROUTINE wave_propogation_fortran