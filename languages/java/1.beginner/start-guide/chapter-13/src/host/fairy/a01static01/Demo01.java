/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-31 00:10:33 UTC+08:00
 ****************************************************/
package host.fairy.a01static01;

/**
 * @author Lionel Johnson
 */
public class Demo01 {
    public static void main(String[] args) {
        Student student1 = new Student("Alice", 18, "女");
        Student student2 = new Student("Alex", 22, "男");
        
        Student.teacher = "Mr.Johnson";
        student1.study();
        System.out.println(student1.show());
        System.out.println(student2.show());
    }
}
