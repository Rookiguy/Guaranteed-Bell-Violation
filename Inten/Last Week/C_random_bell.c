#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

float p=0;

//function for dot product
float dotprod(float a[], float b[]){
   float sum=0;
   for(int l=0;l<3;l++){
      //printf("%f\n",a[l]*b[l]);
      sum=sum+a[l]*b[l];
   }   
      return sum;
   
}
//function returning Norm
float norm(float a[]){
   float kl=0;
   for(int fg=0;fg<3;fg++){
      kl=kl+a[fg]*a[fg];
   }
   return kl;
}

//Function returning Expectation Value
float E(float a[], float b[]){
   float temp;
   //float p=0.49;
   float t1;
   t1=p-p*p;
   temp=a[2]*b[2]-(2*pow(t1,0.5)*(a[0]*b[0]-a[1]*b[1]));
   return temp;
}

int main() 
{  
   srand(time(NULL));
   for(int k=0;k<51;k++){
      clock_t start, end;
      start = clock();
      double count=1000000;
      double count1=1000000;
      for(double w=0;w<1000000;w++){  
         float a1[3]={0,0,0};
         float a2[3]={0,0,0};
         float a3[3]={0,0,0};
         float b1[3]={1,0,0};
         float b2[3]={0,1,0};
         float b3[3]={0,0,1};

         float ta1,ta2,ta3,tb1,tb2,tb3;

         double u1 = (((double)rand())/(double)RAND_MAX);
         double v1 = (((double)rand())/(double)RAND_MAX);
         double theta1 = 2 * M_PI * u1;
         double phi1 = acos(2*v1-1);
         double x1   = sin(theta1)*cos(phi1);
         double y1   = sin(theta1)*sin(phi1);
         double z1   = cos(theta1);
         a1[0]=x1;
         a1[1]=y1;
         a1[2]=z1;

         //printf("[%lf,%lf,%lf],\n",x1,y1,z1);

         
         double u2 = (((double)rand())/(double)RAND_MAX);
         double v2 = (((double)rand())/(double)RAND_MAX);
         double theta2 = 2 * M_PI * u2;
         double phi2 = acos(2*v2-1);
         double x2   = sin(theta2)*cos(phi2);
         double y2   = sin(theta2)*sin(phi2);
         double z2   = cos(theta2);
         b1[0]=x2;
         b1[1]=y2;
         b1[2]=z2;
         //printf("[%lf,%lf,%lf],\n",x,y,z);
         

         for(int i=0;i<3;i++){
            //a1[i]=rand();
            a2[i]=rand();
            a3[i]=rand();

            //b1[i]=rand();
            b2[i]=rand();
            b3[i]=rand();
         }

         //ta1=(pow((pow(a1[0],2)+pow(a1[1],2)+pow(a1[2],2)),-0.5));
         ta2=(pow((pow(a2[0],2)+pow(a2[1],2)+pow(a2[2],2)),-0.5));
         ta3=(pow((pow(a3[0],2)+pow(a3[1],2)+pow(a3[2],2)),-0.5));

         //tb1=(pow((pow(b1[0],2)+pow(b1[1],2)+pow(b1[2],2)),-0.5));
         tb2=(pow((pow(b2[0],2)+pow(b2[1],2)+pow(b2[2],2)),-0.5));
         tb3=(pow((pow(b3[0],2)+pow(b3[1],2)+pow(b3[2],2)),-0.5));

         for(int i = 0; i<3; i++){  
            //a1[i]=a1[i]*ta1;
            a2[i]=a2[i]*ta2;
            a3[i]=a3[i]*ta3;

            //b1[i]=b1[i]*tb1;
            b2[i]=b2[i]*tb2;
            b3[i]=b3[i]*tb3;
         }

         float da12,da13,da23,db12,db13,db23;

         da12=dotprod(a1,a2);
         for(int i=0;i<3;i++){
            a2[i]=a2[i]-da12*a1[i];
         }
         
         float temp1;
         temp1=(pow((pow(a2[0],2)+pow(a2[1],2)+pow(a2[2],2)),-0.5));
         for(int i=0;i<3;i++){
            a2[i]=a2[i]*temp1;
         }

         da13=dotprod(a1,a3);
         da23=dotprod(a2,a3);
         for(int i=0;i<3;i++){
            a3[i]=a3[i]-da13*a1[i]-da23*a2[i];
         }
         float temp2;
         temp2=(pow((pow(a3[0],2)+pow(a3[1],2)+pow(a3[2],2)),-0.5));
         for(int i=0;i<3;i++){
            a3[i]=a3[i]*temp2;
         }
         
         db12=dotprod(b1,b2);
         for(int i=0;i<3;i++){
            b2[i]=b2[i]-db12*b1[i];
         }
         float temp3;
         temp3=(pow((pow(b2[0],2)+pow(b2[1],2)+pow(b2[2],2)),-0.5));
         for(int i=0;i<3;i++){
            b2[i]=b2[i]*temp3;
         }

         db13=dotprod(b1,b3);
         db23=dotprod(b2,b3);
         for(int i=0;i<3;i++){
            b3[i]=b3[i]-db13*b1[i]-db23*b2[i];
         }
         
         float temp4;
         temp4=(pow((pow(b3[0],2)+pow(b3[1],2)+pow(b3[2],2)),-0.5));
         for(int i=0;i<3;i++){
            b3[i]=b3[i]*temp4;
         }
         
         /*
         float t1[3]={pow(2,2),pow(2,2),pow(2,2)};
         float t2[3]={pow(2,2),pow(2,2),pow(2,2)};
         printf("[[%f, %f, %f],\n",a1[0],a1[1],a1[2]);
         printf("[%f, %f, %f],\n",a2[0],a2[1],a2[2]);
         printf("[%f, %f, %f]]\n",a3[0],a3[1],a3[2]);
         printf("\n");
         printf("[[%f, %f, %f],\n",b1[0],b1[1],b1[2]);
         printf("[%f, %f, %f],\n",b2[0],b2[1],b2[2]);
         printf("[%f, %f, %f]]\n",b3[0],b3[1],b3[2]);
         printf("%f",dotprod(t1,t2));
         */








         float bell[36];

         bell[0]=+E(a1,b1)+E(a1,b2)+E(a2,b1)-E(a2,b2);
         bell[1]=+E(a1,b1)+E(a1,b2)-E(a2,b1)+E(a2,b2);
         bell[2]=+E(a1,b1)-E(a1,b2)+E(a2,b1)+E(a2,b2);
         bell[3]=-E(a1,b1)+E(a1,b2)+E(a2,b1)+E(a2,b2);
         
         bell[4]=+E(a1,b1)+E(a1,b3)+E(a2,b1)-E(a2,b3);
         bell[5]=+E(a1,b1)+E(a1,b3)-E(a2,b1)+E(a2,b3);
         bell[6]=+E(a1,b1)-E(a1,b3)+E(a2,b1)+E(a2,b3);
         bell[7]=-E(a1,b1)+E(a1,b3)+E(a2,b1)+E(a2,b3);
                                       
         bell[8]=+E(a1,b2)+E(a1,b3)+E(a2,b2)-E(a2,b3);
         bell[9]=+E(a1,b2)+E(a1,b3)-E(a2,b2)+E(a2,b3);
         bell[10]=+E(a1,b2)-E(a1,b3)+E(a2,b2)+E(a2,b3);
         bell[11]=-E(a1,b2)+E(a1,b3)+E(a2,b2)+E(a2,b3);
                                 
         bell[12]=+E(a1,b1)+E(a1,b2)+E(a3,b1)-E(a3,b2);
         bell[13]=+E(a1,b1)+E(a1,b2)-E(a3,b1)+E(a3,b2);
         bell[14]=+E(a1,b1)-E(a1,b2)+E(a3,b1)+E(a3,b2);
         bell[15]=-E(a1,b1)+E(a1,b2)+E(a3,b1)+E(a3,b2);
                                    
         bell[16]=+E(a1,b1)+E(a1,b3)+E(a3,b1)-E(a3,b3);
         bell[17]=+E(a1,b1)+E(a1,b3)-E(a3,b1)+E(a3,b3);
         bell[18]=+E(a1,b1)-E(a1,b3)+E(a3,b1)+E(a3,b3);
         bell[19]=-E(a1,b1)+E(a1,b3)+E(a3,b1)+E(a3,b3);
                        
         bell[20]=+E(a1,b2)+E(a1,b3)+E(a3,b2)-E(a3,b3);
         bell[21]=+E(a1,b2)+E(a1,b3)-E(a3,b2)+E(a3,b3);
         bell[22]=+E(a1,b2)-E(a1,b3)+E(a3,b2)+E(a3,b3);
         bell[23]=-E(a1,b2)+E(a1,b3)+E(a3,b2)+E(a3,b3);
                        
         bell[24]=+E(a2,b1)+E(a2,b2)+E(a3,b1)-E(a3,b2);
         bell[25]=+E(a2,b1)+E(a2,b2)-E(a3,b1)+E(a3,b2);
         bell[26]=+E(a2,b1)-E(a2,b2)+E(a3,b1)+E(a3,b2);
         bell[27]=-E(a2,b1)+E(a2,b2)+E(a3,b1)+E(a3,b2);
                                          
         bell[28]=+E(a2,b1)+E(a2,b3)+E(a3,b1)-E(a3,b3);
         bell[29]=+E(a2,b1)+E(a2,b3)-E(a3,b1)+E(a3,b3);
         bell[30]=+E(a2,b1)-E(a2,b3)+E(a3,b1)+E(a3,b3);
         bell[31]=-E(a2,b1)+E(a2,b3)+E(a3,b1)+E(a3,b3);
                                                            
         bell[32]=+E(a2,b2)+E(a2,b3)+E(a3,b2)-E(a3,b3);
         bell[33]=+E(a2,b2)+E(a2,b3)-E(a3,b2)+E(a3,b3);
         bell[34]=+E(a2,b2)-E(a2,b3)+E(a3,b2)+E(a3,b3);
         bell[35]=-E(a2,b2)+E(a2,b3)+E(a3,b2)+E(a3,b3); 

         float maxx=0;
         for(int jh=0;jh<36;jh++){
            if(bell[jh]<0){
               bell[jh]=-bell[jh];
            }
            if(maxx<bell[jh]){
               maxx=bell[jh];
            }
         }   
         //printf("%f\n",maxx);
         if(maxx<2){
            count1=count1-1;
            //printf("maxx<2, %f\n",maxx);
         }
      
      }
      end = clock();
      double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
      //double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
      printf("Probability of Violation is %f for p=%f\n",count1/count,p);   
      //printf("finished %f",time_spent);
      p=p+0.01;
   
   }
   return 0; 
} 
