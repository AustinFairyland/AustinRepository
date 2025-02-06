/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 01:32:13 UTC+08:00
 *****************************************************/
package ltd.fairy.extend;

/**
 * @author Lionel Johnson
 */
public class Test {

    static void testStudent() {
        Student student = new Student("Lionel", 18, "清华大学");
        String eat = student.eat("饭");
        System.out.println(eat);
        System.out.println(student.getName());
    }

    public static void main(String[] args) {
        testStudent();
    }
}
