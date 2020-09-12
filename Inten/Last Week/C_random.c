#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <conio.h>

/*
double get_random() { return (((double)rand())/(double)RAND_MAX); }

double get_rand_pi() { return (((double)rand() / (double)RAND_MAX)*3.14); }
*/
int main()
{   srand(time(NULL));
    double a[10000];
    double b[10000];
    double c[10000];
    for(int l=0;l<10000;l++)
    {
        double u = (((double)rand())/(double)RAND_MAX);
        double v = (((double)rand())/(double)RAND_MAX);
        double theta = 2 * M_PI * u;
        double phi = acos(2*v-1);
        double x   = sin(theta)*cos(phi);
        double y   = sin(theta)*sin(phi);
        double z   = cos (theta);
        a[l]=x;
        b[l]=y;
        c[l]=z;
        //printf("[%lf,%lf,%lf],\n",x,y,z);
    }

    FILE *f = fopen("work.txt", "w");
    for(int hk=0;hk<10000;hk++)
    {
        fprintf(f,"[%lf, %lf, %lf],\n",a[hk],b[hk],c[hk]);
    }
    fclose(f);
    return 0;
}