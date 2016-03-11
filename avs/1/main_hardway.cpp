//this file uses more low-level implementation of task

/*compile with:
 * g++ source.c -pedantic -lncurses -std=c++11 -masm=intel -m32*/
#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <vector>

#include "input.h"
#include "equation_hardway.h"

int main() {
    std::vector <double> result;
    double A;
    double B;
    double C;
    initscr();
    noecho();
    clear();
    printw("input A \n");
    refresh();
    do {
        clear();
        refresh();
        printw("input A \n");
        refresh();
        A = input_double();
        printw("input B \n");    
        refresh();
        B = input_double();
        printw("input C \n");    
        refresh();
        C = input_double();
    
        if (A == 0) { //handling A = 0
            printw("A = 0");
            refresh();
            continue;
        }

        result = hard_solve(A, B, C);
        if (result[0] == 0) {
            printw("no solutions");
            refresh();
        }

        if (result[0] == 1) {
            printw("%f", result[1]);
            refresh();
        }

        if (result[0] == 2) {
            printw("%f", result[1]);
            printw(", ");
            printw("%f", result[2]);
            refresh();
        } 

        printw("\n");
        printw("press any key to continue");
        printw("\n");
        printw("press ESC key to quit");
        refresh();
    } while (getchar() != 27);
    endwin();
}
