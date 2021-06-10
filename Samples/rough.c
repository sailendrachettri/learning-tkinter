
#include <stdio.h>

int main()
{
    /*
   for(int i=1; i<=3; i++)
   {
       for(int j=1; j<=10; j++)
       {
           printf("%d ", i*j);
       }
       printf("\n");
   }


    int i = 1;

    while(i<=3)
    {
        int j = 1;
        while(j<=10)
        {
            printf("%d ", i*j);
            j++; 
        }
        printf("\n");
        i++;
    } 
    */
    int i = 1;
    do
    {
        int j = 1;
        do
        {
            printf("%d ", i * j);
            j++;
        } while (j <= 10);

        printf("\n");
        i++;
    } while (i <= 3);

    return 0;
}