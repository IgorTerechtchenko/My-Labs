#include<iostream>
#include<string>
#include<vector>
#include<cstring>
using namespace std;

int main() {
    string line;
    int tmp_pair;
    int tmp;
    vector <int> counter_array;
    vector <int> tokens;
    int request_count;
    cin >> line;
    char char_array[line.length()];
    strcpy(char_array, line.c_str());

    for(unsigned int i = 0; i < line.length(); i++) {
        counter_array.push_back(0);
    }

    cin >> request_count;
    for (int i = 0; i < request_count; i++) {
        for (unsigned int i = 0; i < 2; i++) {
            cin >> tmp_pair;
            tokens.push_back(tmp_pair);
        }
        if (tokens[0] > tokens[1]) {
            tmp = tokens[1];
            tokens[1] = tokens[0];
            tokens[0] = tmp;
        }
        counter_array[tokens[0] - 1] += 1;
        counter_array[tokens[1]] += 1;
        tokens.clear();
    }
    int counter = 0;
    for (int i = 0; i < line.length(); i++) {
        counter += counter_array[i];
        if (counter % 2 != 0) {
            if (64 < line[i] && line[i] < 91) {
                char_array[i] = char_array[i] + 32;
            } else {
                if (96 < line[i] && line[i] < 123) {
                    char_array[i] = char_array[i] - 32;
                }
            }
        }
    }

    for (int i = 0; i < line.length(); i++) {
        cout << char_array[i];
    }
    cout << "\n";
    return 0;
}
