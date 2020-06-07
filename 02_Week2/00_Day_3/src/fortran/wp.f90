

SUBROUTINE wave_propogation(num_steps, scale, damping, initial_P, stop_step, P)
  IMPLICIT NONE
  INTEGER size_x,size_Y,i,j,k,step
  REAL PI, omega
  INTEGER, INTENT(in)  :: num_steps, scale, stop_step !input
  REAL, INTENT(in) :: damping, initial_P !input
  REAL, INTENT(out) :: P(2 * scale + 1,2 * scale + 1) ! output
  REAL, DIMENSION(2 * scale + 1,2 * scale + 1,4) :: V

  size_x = 2 * scale + 1
  size_Y = 2 * scale + 1

  PI = 3.14159
  omega = 3.0 / (2.0 * PI)

  DO k=1,4
     DO j=1,size_x
        DO i=1,size_x
           P(i,j) = 0.0
           V(i,j,k) = 0.0
        END DO
     END DO
  END DO

  P(scale,scale) = initial_P

  DO step = 1,num_steps
     IF(step <= stop_step) THEN
        P(scale,scale) = initial_P * SIN(omega * step)
     ENDIF

     DO j=1,size_x
        DO i=1,size_x
           V(i,j,1) = MERGE(V(i,j,1) + P(i,j) - P(i - 1,j), P(i,j), i > 1)
           V(i,j,2) = MERGE(V(i,j,2) + P(i,j) - P(i,j + 1), P(i,j), j < size_x - 1)
           V(i,j,3) = MERGE(V(i,j,3) + P(i,j) - P(i + 1,j), P(i,j), i < size_y - 1)
           V(i,j,4) = MERGE(V(i,j,4) + P(i,j) - P(i,j - 1), P(i,j), j > 1)
        END DO
     END DO

     DO j=1,size_x
        DO i=1,size_x
           P(i,j) = P(i,j) - 0.5 * damping * (V(i,j,1) + V(i,j,2) + V(i,j,3) + V(i,j,4))
        END DO
     END DO
  END DO

END SUBROUTINE wave_propogation
