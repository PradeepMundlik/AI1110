//2.4 mean and variance
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int main()
{
    printf("Mean=%lf\n",mean("gau.dat"));
    printf("Variance=%lf\n",var("gau.dat"));
    return 0;
}