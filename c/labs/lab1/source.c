#include <stdio.h>

/*
Set of numbers is entered. Minimal, maximal & average value of entered numbers
 should be written after every entered number.
*/

// -std=c99 flag is used when compiling

int main()
{
    double input;
    double max;
    double min;
    double average;
    double sum = 0; 
    
    int counter = 1;	

	printf("enter values, or enter any other sybol to exit\n");	

	while(scanf("%lf", &input)){
	
	printf("enter values, or enter any other sybol to exit\n");
			
	if(counter == 1) { 	
		min = input;
		max = input;
	}
		
	if(input < min) { 
		min = input;
	}	
	
	if(input > max) {  
		max = input;
	}
		
	sum += input;
	average = sum / counter;

	counter++;	
	
	printf( "minimal value %0.3lf \n",min );
	printf( "maximal value %0.3lf \n",max );
	printf( "average value %0.3lf \n",average );
    }
    return 0;
}
