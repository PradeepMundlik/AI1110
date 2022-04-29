/************************
Name: Pradeep Mundlik
Roll no: AI21BTECH11022
************************/

/***** AI1110 Assignment 1 *****/
/***** Question 6(b) ICSE 2019 *****/

#include <stdio.h>
#include <math.h>
int main()
{
    int a;
    int r;
    int l;

    printf("Enter first term of GP : ");
    scanf("%d", &a);
    printf("Enter last term of GP : ");
    scanf("%d", &l);
    printf("Enter common ratio of GP : ");
    scanf("%d", &r);
    printf("\n\n");

    /***************************************************
        a, a*r, a*r^2, a*r^3,......, a*r^(n-1)
        nth term = a*r^(n-1)
        l = a*r^(n-1)
        r^(n-1) = (l/a)
        L/(r*r*r*r*....(n-1 times r)) = a
        So, if we continously divide l by r until it becomes equal to a,
        and count all operations needed then it will give n-1.
    ***************************************************/

    int n = 1;
    while (l != a)
    {
        l = l / r;
        n++;
    }

    printf("Number of terms in GP is %d\n", n);

    // To caclulate sum of all n terms, we simply use for loop
    int sum = 0;
    int term = a;
    for (int i = 0; i < n; i++)
    {
        sum = sum + term;
        term = term * r;
    }
    printf("The sum of all terms is %d\n", sum);

    return 0;
}