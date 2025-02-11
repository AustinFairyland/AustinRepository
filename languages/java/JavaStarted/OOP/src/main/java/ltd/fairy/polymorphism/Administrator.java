/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-11 02:16:49 UTC+08:00
 *****************************************************/
package ltd.fairy.polymorphism;

/**
 * @author Lionel Johnson
 */
public class Administrator extends Person {

    public Administrator(String name, int age) {
        super(name, age);
    }

    @Override
    public void show() {
        System.out.println("管理员信息: 姓名：" + this.getName() + "，年龄：" + this.getAge());
    }
}
