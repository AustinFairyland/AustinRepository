/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 22:47:05 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.ArrayList;

/**
 * @author Lionel Johnson
 */
public class ArrayListDemo3 {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();

        Student alice = new Student("Alice", 18);
        Student bob = new Student("Bob", 19);
        
        students.add(alice);
        students.add(bob);

        for (Student student : students) {
            System.out.println("Name: " + student.name + ", Age: " + student.age);
        }
    }
}

class Student {
    String name;
    int age;
    
    public Student() {
    }
    
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
