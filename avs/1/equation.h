#include <vector>

#include "arithmetics.h"

double discriminant(double a, double b, double c) {
    return co_add(co_mul(b, b), co_neg(co_mul(co_mul(4, a), c))); //D = b^2 - 4ac
}

std:: vector <double> solve(double a, double b, double c) {
    double TWO = 2;
    double D = discriminant(a, b, c);
    std::vector <double> output; 

    if (D == 0) {                                          //1 solution
        output.push_back(1);                               //solution_number
        output.push_back(co_div(co_neg(b), co_mul(2, a))); //x = -b/(2*a)
    }

    if (D > 0) {
        output.push_back(2);                               //solution_number
        output.push_back(co_div(                           //x1 = (-b - sqr(D))/(2*a)
            co_add(co_neg(b), co_neg(co_sqr(D))),          //yes, i do think this is better than assembly code
            co_mul(2, a)                                   
        ));
        output.push_back(co_div( //x2
            co_add(co_neg(b), co_sqr(D)), 
            co_mul(2, a)
        ));
    }

    if (D < 0) {
        output.push_back(0); //no solutions
    }
    return output;
}
