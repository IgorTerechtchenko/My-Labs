/*compile with:
 * g++ source.c -pedantic -lncurses -std=c++11*/
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <vector>
#include <ncurses.h>

double A;
double B;
double C;

double input_float() { 
    char temp;
    std::vector <char> output; 
    bool minus_entered = false;
    bool point_entered = false;
    bool char_entered = false;
    bool zero_entered = false;
    while (output.size() < 10) {
        temp = getchar();
        if (((temp == 13) && (char_entered)) || ((temp == 13) && (zero_entered) && (!minus_entered))) {  
            break;
        }
   
        if ((temp == '-') && (!char_entered) && (!zero_entered) && (!minus_entered)) {
            output.push_back(temp);
            minus_entered = true;
            printw("%c", temp); 
        }

        if (isdigit(temp)) {
            if(temp == '0') {
                zero_entered = true;
            } else {
                char_entered = true; 
            }
            output.push_back(temp); 
            printw("%c", temp); 
            refresh();
        }
        if (temp == '+') {
            refresh();
        }

        if ((temp == '.') && ((char_entered) || (zero_entered)) && (!point_entered)) {
            output.push_back(temp);
            point_entered = true;
            printw("%c", temp); 
        }
        
        if ((temp == '0') && (zero_entered) && (!point_entered)) {
            continue;
        }

        if ((temp == 127) && (output.size() > 0)) { //backspace handling
            if(output.back() == '.') {
                point_entered = false;
            }
            
            if(output.back() == '-') {
                minus_entered = false;
            }
            
            output.pop_back();
             
            if (!(std::find(output.begin(), output.end(), '0') !=  output.end())) {
                zero_entered = false;
            }

            if(output.empty()) {
                char_entered = false;
            }
            printw("\b");
            printw(" ");
            printw("\b");
        }
        move(2,0);
        printw("c");
        printw("z");
        printw("m");
        move(3,0);
        printw("%d", char_entered);
        printw("%d", zero_entered);
        printw("%d", minus_entered);
        move(1,output.size());
        refresh();
    }
    output.push_back('\0');
    return atof(&output[0]);    
}

int main() {
    initscr();
    noecho();
    printw("enter A:\n");
    refresh(); 
    A = input_float();
    printw("\n");
    printw("%f", A);
    refresh();
    getchar();
    endwin();
} 
