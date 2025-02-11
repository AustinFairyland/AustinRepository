/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-11 02:17:24 UTC+08:00
 *****************************************************/
package ltd.fairy.polymorphism;

/**
 * @author Lionel Johnson
 */
public class Test {

    public static void main(String[] args) {
        // 创建学生对象
        register(new Student("张三", 18));

        // 创建教师对象
        register(new Teacher("李四", 30));

        // 创建管理员对象
        register(new Administrator("王五", 40));

    }

    static void register(Person person) {
        person.show();
    }
}
