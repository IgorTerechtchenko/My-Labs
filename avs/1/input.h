#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <vector>
#include <ncurses.h>

double input_double() {
    char temp;
    std::vector <char> output;
    bool minus_entered = false;
    bool point_entered = false;
    bool char_entered = false;
    bool zero_entered = false;
    while (output.size() < 10) { //limit to avoid overflow
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
        refresh();
    }
    output.push_back('\0');
    clear();
    refresh();
    return atof(&output[0]);
}
