#include<vector>
#include<stdio.h>
double hard_discriminant(double a, double b, double c) {
    double D;
    double FOUR = 4;
    __asm__( 
        ".intel_syntax noprefix \n" //use intel syntax instead of AT&T
        "finit \n"   //initialize coprocessor
        
        "fld %2 \n" //b * b
        "fmul %2 \n" //st(0) = b * b
        
        "fld %1 \n" //st(0) = a; st(1) = b^2
        "fmul %3 \n"//st(0) = a * c
        "fmul %4 \n"//st(0) = 4*a*c
        "fsubr st(0), st(1) \n"//st(0) = st(1) - st(0) = b^2 - 4*a*c  
        
        "fst %0 \n" //loading st(0) into D
        : "=g"(D)
        : "g"(a), "g"(b), "g"(c), "g"(FOUR)
    );

    return D;
}
std:: vector <double> hard_solve(double a, double b, double c) {
    double TWO = 2;
    double ZERO = 0;
    double D = hard_discriminant(a, b, c);
    double temp;
    std::vector <double> output; 

    if (D == 0) {                                          //1 solution
        output.push_back(1);                               //solution_number
        __asm__( 
            ".intel_syntax noprefix \n" //use intel syntax instead of AT&T
            "finit \n"   //initialize coprocessor
            "fld %4 \n"  //st(0) = 0
            "fsub %2 \n" //st(0) = -b
            "fld %1 \n"  //st(0) = a, st(1) = -b
            "fmul %3 \n" //st(0) = st(0) * TWO = a * 2
            "fdiv st(0), st(1) \n" //st(0) = st(1)/st(0) = -b/2*a
            "fst %0 \n" //load st(0) to temp 
            : "=g"(temp)
            : "g"(a), "g"(b), "g"(TWO), "g"(ZERO)
        );
        output.push_back(temp);
        return output;
    }

    if (D > 0) {
        output.push_back(2);            //solution_number
        __asm__(                        //x1 = (-b - sqr(D))/(2*a)
            ".intel_syntax noprefix \n" //use intel syntax instead of AT&T
            "finit \n"   //initialize coprocessor
            "fld %4 \n"  //st(0) = 0
            "fsub %2 \n" //st(0) = st(0) - b = -b
            "fld %3 \n"  //st(0) = D, st(1) = -b
            "fsqrt \n"   //st(0) = sqrt(D)
            "fsubr st(0), st(1) \n" //st(0) = st(1) - st(0) = -b - sqrt(D)
            "fld %1 \n"  //st(0) = a, st(1) = -b - sqrt(D)
            "fmul %5 \n" //st(0) = a * 2
            "fdivr st(0), st(1) \n" //st(0) = st(1)/st(0) = (-b - sqrt(D)) / 2*a
            "fst %0 \n" //load st(0) to temp
            : "=g"(temp)
            : "g"(a), "g"(b), "g"(D), "g"(ZERO), "g"(TWO)
        );

        output.push_back(temp);
        
        __asm__(                        //x1 = (-b + sqr(D))/(2*a)
            ".intel_syntax noprefix \n" //use intel syntax instead of AT&T
            "finit \n"   //initialize coprocessor
            "fld %4 \n"  //st(0) = 0
            "fsub %2 \n" //st(0) = st(0) - b = -b
            "fld %3 \n"  //st(0) = D, st(1) = -b
            "fsqrt \n"   //st(0) = sqrt(D)
            "fadd st(0), st(1) \n" //st(0) = st(1) - st(0) = -b - sqrt(D)
            "fld %1 \n"  //st(0) = a, st(1) = -b - sqrt(D)
            "fmul %5 \n" //st(0) = a * 2
            "fdivr st(0), st(1) \n" //st(0) = st(1)/st(0) = (-b - sqrt(D)) / 2*a
            "fst %0 \n" //load st(0) to temp
            : "=g"(temp)
            : "g"(a), "g"(b), "g"(D), "g"(ZERO), "g"(TWO)
        );

        output.push_back(temp);
    }

    if (D < 0) {
        output.push_back(0); //no solutions
    }
    return output;
}
