/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-11 02:14:30 UTC+08:00
 *****************************************************/
package ltd.fairy.polymorphism;

/**
 * @author Lionel Johnson
 */
public class Teacher extends Person {

    public Teacher(String name, int age) {
        super(name, age);
    }
    
    public void show() {
        System.out.println("教师信息: 姓名：" + this.getName() + "，年龄：" + this.getAge());
    }
}
