/* 1.4 mean and variance */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int main()
{
    //mean
    printf("Mean=%lf\n",mean("uni.dat"));
    //variance
    printf("Variance=%lf",var("uni.dat"));
    return 0;
}
