double co_add(double a, double b) {
    double output;
    __asm__(
        ".intel_syntax noprefix \n" //use intel syntax instead of AT&T
        "finit \n"   //initialize coprocessor 
        "fld %1 \n"  //load a to st(0)
        "fadd %2 \n" //add b to st(0). result stored in st(0)
        "fst %0 \n"  //load st(0) to output
        : "=g" (output) //%0
        : "g" (a), "g" (b) //%1, %2
    );
    return output;
}

double co_mul(double a, double b) {
   double output;
    __asm__(
        ".intel_syntax noprefix \n"  
        "finit \n" 
        "fld %1 \n"
        "fmul %2 \n" //mul st(0) by b, result stored in st(0)
        "fst %0 \n" 
        : "=g" (output)
        : "g" (a), "g" (b)
    );
    return output;
}

double co_div(double a, double b) {
    double output;
    __asm__(
        ".intel_syntax noprefix \n" 
        "finit \n" 
        "fld %1 \n" 
        "fdiv %2 \n" //div st(0) by b. result stored in st(0)
        "fst %0 \n"
        : "=g" (output)
        : "g" (a), "g" (b)
    );
    return output;
}

double co_sqr(double a) {
   double output;
    __asm__(
        ".intel_syntax noprefix \n"
        "finit \n"
        "fld %1 \n"
        "fsqrt \n" //sqr(st(0)). result stored in st(0)
        "fst %0 \n" 
        : "=g" (output)
        : "g" (a)
    );
    return output;

}

double co_neg(double a) { //return -a
    double TWO = 2.0; //used because i can't pass num literal directly into inline
    double output;
    __asm__(
        ".intel_syntax noprefix \n"
        "finit \n"
        "fld %1 \n" //a * 2
        "fmul %2 \n" //st(0) = a * 2
        "fld %1 \n" //st(0) = a, st(1) = a * 2
        "fsub st(0), st(1) \n" //st(0) = st(0) - st(1)
        "fst %0 \n"
        : "=g" (output)
        : "g" (a), "g"(TWO)
    );
    return output;
}
