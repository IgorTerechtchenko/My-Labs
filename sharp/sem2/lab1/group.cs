using System;
using System.Collections;
using System.Collections.Generic;

class Group: IEnumerable <Student> {
    List<Student> students = new List<Student>();
    
    public int Count() {
        return students.Count;
    }  

    public void Add(Student new_student) {
        students.Add(new_student);
    }
    
    public void Remove(Student student_to_rm) {
        students.Remove(student_to_rm);
    }
    
    public bool Exists(string fname) {
        return this.students.Exists(x => x.getname == fname);
    }  
 
    public int Find(string fname) {
        return this.students.FindIndex(x => x.getname == fname);
    }
 
    public float getaverage_mark() {
        float mark = 0;
        foreach (Student i in students) {
            mark += i.getaverage_mark;
        }
        return mark/students.Count;
    }

    public float getaverage_mark(string key) {
        float mark = 0; 
        foreach (Student i in students) {
            mark += i.marks[key];
        }
        return mark/students.Count;
    }

    public int Exam() {
        int students_removed = 0; 
        for (int i = 0; i < students.Count; i++) { 
            students.Remove(students.Find(x => x.is_to_discharge() == true));
            students_removed++;
        }   
        return students_removed;
    }
        
    public IEnumerator<Student> GetEnumerator() {
        foreach (Student i in students) {
            yield return i;
        }
    }
     
    IEnumerator IEnumerable.GetEnumerator() {
        return GetEnumerator();
    }
}

