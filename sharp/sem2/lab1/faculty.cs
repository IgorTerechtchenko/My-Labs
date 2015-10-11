using System;
using System.Collections;
using System.Collections.Generic;

class Faculty: IEnumerable <Group> {
    List<Group> groups = new List<Group>();
   
    public void Add(Group new_group) {
        groups.Add(new_group);
    }    
    
    public void Remove(Group group_to_remove) {
        groups.Remove(group_to_remove); 
    }

    public float getaverage_mark() {
        float mark = 0;
        int counter = 0;
        foreach (var i in groups) {
            foreach (Student j in i) {
                mark += j.getaverage_mark; //using getaverage_mark method from Group
                counter++;
            }
        }    
        return mark/counter;
    }
    
    public float getaverage_mark(string key) {
        float mark = 0;
        int counter = 0;
        
        foreach (Group i in groups) {
            i.getaverage_mark(key); 
            counter += i.Count();
        }
        return mark/counter;
    }

    public IEnumerator<Group> GetEnumerator() {
        foreach (Group i in groups) {
           yield return i;
        }
    }
 
    IEnumerator IEnumerable.GetEnumerator() {
        return GetEnumerator();
    }
}
