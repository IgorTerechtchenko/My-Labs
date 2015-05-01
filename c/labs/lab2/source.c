/*TRIANGLE
*this program allows user to enter coordinates of triangle points,
*calculate its perimeter, square, incircled and circumcircled circles
*length and find out its type
*it does not allow user to access functions befor entering correct input
*/

#include <stdio.h>
#include <math.h>

struct point { //structure used for storing point coordinates
	int x;
	int y;	
};


double sidelength(struct point p1, struct point p2) { // function for calculating side length
	if (p1.x == p2.x && p1.y == p2.y) {
		printf("bad input: points have same coordinates\nplease try again\n");
	}

	return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}


double perimenter(float side_a, float side_b, float side_c) { // function for calculating perimeter
	return side_a + side_b + side_c;
}


double square(float side_a, float side_b, float side_c) { //function for calculating triangle square
	double semp = perimenter(side_a, side_b, side_c) / 2;

	return sqrt(semp * (semp - side_a) * (semp - side_b) * (semp - side_c));
}


double incircleradius (float side_a, float side_b, float side_c) { //function for calculating inscribed circle radius 
	double semp = perimenter(side_a, side_b, side_c) / 2;
	
	return sqrt((semp - side_a) * (semp - side_b) * (semp - side_c) / semp);
}


double circumcircleradius (float side_a, float side_b, float side_c) { //function for calculating circumscribed circle radius
	double semp = perimenter(side_a, side_b, side_c) / 2;

	return (side_a * side_b * side_c) 	/ 4 * sqrt(semp * (semp - side_a) * (semp - side_b) * (semp - side_c));
}


void triangletype (float side_a, float side_b, float side_c) { //function finds out entered triangle type
	
	double hypotenuse;
	double cathetus1;
	double cathetus2;
	
	bool notscalene = false; //indicates if triagle is rightangled 

	float epsilon = 0.01; //used for aproximate comparison
	
	if (side_a > side_b && side_a > side_c) { //finds out the biggest side, and names it hypotenuse
	
		hypotenuse = side_a;
		cathetus1 = side_b;
		cathetus2 = side_c;

	} else if (side_b > side_c && side_b > side_a) {

		hypotenuse = side_b;
		cathetus1 = side_a;
		cathetus2 = side_c;
	
	} else {

		hypotenuse = side_c;
		cathetus1 = side_a;
		cathetus2 = side_b;
	
	}
			
	if (pow(cathetus2, 2) + pow(cathetus1, 2) - pow(hypotenuse, 2) < epsilon) {
		printf("This triangle is right - angled\n"); 
		notscalene = true;	
	}
	
	if (fabs(side_a - side_b) < epsilon && fabs(side_b - side_c) < epsilon) {
		printf("This triangle is equilaterial\n"); 
		notscalene = true;
	}
		
	if (fabs(side_a - side_b) < epsilon || fabs(side_a - side_c) < epsilon || fabs(side_b - side_c) < epsilon) {
		printf("This triangle is isosceles triangle\n"); 
		notscalene = true;
	}
	
	if(side_a != side_b && side_a != side_c && side_b != side_c && notscalene == false) {
		printf("This triangle is scalene\n");
	}
}


bool check(int side_a, int side_b, int side_c) { //checks if triangle evaulation is executed

	if (side_a + side_b < side_c || side_a + side_c < side_b || side_b + side_c < side_a) {
		return 0;
	}
	else {
		return 1;
	}

} 


void menu() {
	
	printf("Enter 1 to see triangle type\n");
	printf("Enter 2 to see triangle perimeter\n");		
	printf("Enter 3 to see triangle square\n");
	printf("Enter 4 to see incircled & circumcircled circles radiuses\n");
	printf("Enter 5 to enter new triangle\n");
	printf("Enter 6 to see program info\n");
	printf("Enter 0 to exit\n");				
}


void version() {	//function displays program info
	printf("Triangle calculator v 1.0 by Igor Tereschenko\n");
}	


int input() { 

	int a = 0; 
	int input;
	
	while(a != 1) {
		a = scanf("%d", &input); //checks, if input is correct
		if (a == 1) {
			return input;
		}
			printf("bad input, please try again\n");
			while(getchar() != '\n');
	}
return 0;
}


enum choice {

	_type = '1',
	_perimeter = '2',
	_square = '3',
	_radius = '4',
	_new = '5',
	_info = '6'
};


int main() {
	
	struct point point_A;
	struct point point_B;
	struct point point_C;

	int choice; //variable used for menu

	double side_a;
	double side_b;
	double side_c;

	bool badinput = true;	//indicator to avoid using program functions, 
							//while input is incorrect
	menu();

	int counter = 1; // used to avoid "default" execution during the first loop iteration
	
	while((choice = getchar()) != '0') { 

		switch (choice) {
			
			case _type: 
				
				if (badinput == true) {
					printf("bad input");
					break;
				} 
				
				triangletype(side_a, side_b, side_c);
				
				menu();						
				break;
			
			case _perimeter: 
				
				if (badinput == true) {
					printf("bad input");
					break;
				}
				
				printf("%f", perimenter(side_a, side_b, side_c));
				printf("\n");	
			
				menu();			
				break;
			
			case _square:
				
				if (badinput == true) {
					printf("bad input");
					break;
				}
				
				printf("%f", square(side_a, side_b, side_c));		
				printf("\n");
			
				menu();			
				break;
			
			case _radius:
				
				if (badinput == true) {
					printf("bad input");
					break;
				}
				
				printf("%f", incircleradius(side_a, side_b, side_c));
				printf("\n");
				printf("%f", circumcircleradius(side_a, side_b, side_c));				
				printf("\n");
			
				menu();	
				break;

			case _new:
				
				printf("enter A point coordinates (x)\n");
				point_A.x = input();
				printf("enter A point coordinates (y)\n");
				point_A.y = input();
				printf("enter B point coordinates (x)\n");
				point_B.x = input();
				printf("enter B point coordinates (y)\n");
				point_B.y = input();
				printf("enter C point coordinates (x)\n");
				point_C.x = input();
				printf("enter C point coordinates (y)\n");
				point_C.y = input();
				
				if (check(side_a, side_b, side_c) == 0) {
					printf("bad input: this triangle can't exist\nplease try again\n");
					badinput = true;
				} 
				
				else {
					badinput = false;
				}			
				
				if ((point_A.x == point_A.y && point_B.x == point_B.y && point_C.x == point_C.y) || //checks if entered points 
					(point_A.x == point_B.x && point_B.x == point_C.x) ||							//belong to the same line
					(point_A.y == point_B.y && point_B.y == point_C.y)) {							
					
					printf("bad input, please try again\n");
					badinput = true;
				}
				
				else {
					badinput = false;
				}
			
				side_a = sidelength(point_A, point_B); //calculating and storing sides length
				side_b = sidelength(point_B, point_C);
				side_c = sidelength(point_A, point_C);	
			
				menu();
				break;				
	
			case _info:
				version();
				
				menu();		
				break;
			
			default:
				
				if (counter == 1) {
					counter++;
					continue;
				}
				
				printf("Incorrect value\n");
				
				menu();
				break;	
			}
	while(getchar() != '\n'); 
	}

return 0;
}
