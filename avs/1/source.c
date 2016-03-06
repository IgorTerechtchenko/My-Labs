#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <vector>
#include <ncurses.h>

char temp;

double A;
float B;
float C;

double input_float() {
    std::vector <char> output; 
    bool input_is_valid = false;
    bool minus_entered = false;
    bool point_entered = false;
    bool char_entered = false;
    while (true) {
        temp = getchar();
        if ((temp == 13) && (char_entered)) { //used to break if enter key is pressed. '\n' won't work 
            break;
        }
   
        if ((temp == '-') && (char_entered == false) && (minus_entered == false)) {
            output.push_back(temp);
            minus_entered = true;
            printw("%c", temp); 
        }

        if (isdigit(temp)) {
            output.push_back(temp); 
            char_entered = true; 
            printw("%c", temp); 
        }

        if ((temp == '.') && (char_entered == true) && (point_entered == false)) {
            output.push_back(temp);
            point_entered = true;
            printw("%c", temp); 
        }
        refresh();
    }
    
    printw("\n"); 

    for (int i = 0;i < output.size(); i ++) {
        printw("%c", output[i]);
    }
    refresh();
    return atof(&output[0]);    
}

int main() {
    initscr();
    noecho();
    A = input_float();
    printw("\n");
    printw("%f", A);
    refresh();
    getchar();
    endwin();
} 
