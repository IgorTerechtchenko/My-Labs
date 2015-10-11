using System;
using System.Collections;
using System.Collections.Generic;

class Faculty: IEnumerable <Group> {
    List<Group> groups = new List<Group>();
   
    public void Add(Group new_group) {
        groups.Add(new_group);
    }    
      
}
