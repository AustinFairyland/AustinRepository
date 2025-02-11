/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-11 02:13:00 UTC+08:00
 *****************************************************/
package ltd.fairy.polymorphism;

/**
 * @author Lionel Johnson
 */
public class Student extends Person {

    public Student(String name, int age) {
        super(name, age);
    }

    @Override
    public void show() {
        System.out.println("学生信息: 姓名：" + this.getName() + "，年龄：" + this.getAge());
    }
}
