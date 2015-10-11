using System;
using System.Collections;
using System.Collections.Generic;

class Program {
   public static void Main() {
        Student Ivan = new Student(3, 3, 1, "Ivan"); 
        Student Stepan = new Student(7, 4, 9, "Stepan");
        Student Zahar = new Student(3, 3, 1, "Zahar");
        Student Pyotr = new Student(4, 5, 5, "Pyotr");

        Group group1 = new Group();
        Group group2 = new Group();

        group1.Add(Ivan); 
        group1.Add(Pyotr);
        group2.Add(Zahar);
        group2.Add(Stepan);
       
        Faculty KSiS = new Faculty();
        KSiS.Add(group1); 
        KSiS.Add(group2); 
   }
}

