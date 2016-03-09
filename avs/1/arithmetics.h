double co_add(double a, double b) {
    double output;
    __asm__(
        ".intel_syntax noprefix \n"
        "finit \n"
        "fld %1 \n"
        "fadd %2 \n"
        "fst %0 \n"
        : "=g" (output)
        : "g" (a), "g" (b)
    );
    return output;
}

double co_mul(double a, double b) {
   double output;
    __asm__(
        ".intel_syntax noprefix \n"
        "finit \n"
        "fld %1 \n"
        "fmul %2 \n"
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
        "fdiv %2 \n"
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
        "fsqrt \n"
        "fst %0 \n"
        : "=g" (output)
        : "g" (a)
    );
    return output;

}

double co_neg(double a) { //return -a
    double TWO = 2.0;
    double output;
    __asm__(
        ".intel_syntax noprefix \n"
        "finit \n"
        "fld %1\n" //a * 2
        "fmul %2 \n"
        "fld %1\n"
        "fsub st(0), st(1) \n"
        "fst %0\n"
        : "=g" (output)
        : "g" (a), "g"(TWO)
    );
    return output;
}
