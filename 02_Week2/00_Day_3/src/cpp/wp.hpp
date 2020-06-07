#include <chrono>
#include <iostream>
#include <math.h>
#ifndef __APPLE__
#include <omp.h>
#endif

void wave_propogation_single_core(int num_steps, int scale, float damping,
                                  float initial_P, int stop_step, float *_P);
