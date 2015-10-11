using System;
using System.Collections.Generic;
class Student {
    
    public Dictionary<string, int> marks;
    string name;
    float average_mark;  

    public string getname {
        get {
            return this.name;
        }
    } 

    public float getaverage_mark {
        get {
            return average_mark;
        }
    }

    public bool is_to_discharge() {
        foreach(var item in marks.Values) {
            if(item < 4) return true;
        }
        return false;
    }

    public Student(int math_mark, int programming_mark, int algorythms_mark, string new_name) {
        name = new_name;
        marks = new Dictionary<string, int>();
        marks.Add("MATH", math_mark);
        marks.Add("PROGRAMMING", programming_mark);
        marks.Add("ALGORYTHMS", algorythms_mark);

        average_mark = (marks["MATH"] + marks["PROGRAMMING"] + marks["ALGORYTHMS"])/3;
    }
}
