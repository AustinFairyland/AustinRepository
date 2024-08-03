/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-31 00:06:13 UTC+08:00
 ****************************************************/
package host.fairy.a01static01;

/**
 * @author Lionel Johnson
 */
public class Student {
    String name;
    int age;
    String gender;
    static String teacher;

    public Student(String name, int age, String gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
    
    public void study() {
        System.out.println(this.name + " is studying.");
    } 
    
    public String show() {
        return "Student: " + this.name + ", " + this.gender + ", " + this.age + ", " + teacher;
    }
}
