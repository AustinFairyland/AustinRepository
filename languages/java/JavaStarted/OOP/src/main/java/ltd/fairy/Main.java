/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 23:44:13 UTC+08:00
 *****************************************************/
package ltd.fairy;

import ltd.fairy.OOP.GirlFriend;
import ltd.fairy.OOP.Phone;
import ltd.fairy.bean.Student;
import ltd.fairy.extend.Ragdoll;

import org.openjdk.jol.info.ClassLayout;

/**
 * @author Lionel Johnson
 */
public class Main {
    static void testPhone() {
        Phone phone = new Phone();
        phone.name = "iPhone 13";
        phone.color = "Blue";
        phone.price = 1399.00;

        System.out.println(phone.call("张山"));


        GirlFriend girlFriend = new GirlFriend("小红", 18, "女");
        girlFriend.sleep();
    }

    static void testStudent() {
        Student.teacherName = "admin";
        Student student = new Student("张三", 18, "男");
        student.show();
        student.study();
    }

    static void testRagdoll() {
        Ragdoll ragdoll = new Ragdoll("布偶猫");
        ragdoll.eat("猫粮");
        ragdoll.drink();
        ragdoll.catchMouse();

        System.out.println(ClassLayout.parseInstance(ragdoll).toPrintable());
    }

    public static void main(String[] args) {
//        testPhone();
//        testStudent();
        testRagdoll();
    }
}
