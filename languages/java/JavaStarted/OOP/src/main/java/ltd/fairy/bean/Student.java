/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 01:02:28 UTC+08:00
 *****************************************************/
package ltd.fairy.bean;

/**
 * @author Lionel Johnson
 */
public class Student {
    String name;
    int age;
    String gender;

    public static String teacherName;

    private Student() {
    }

    public Student(String name, int age, String gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    public String getName() {
        return this.name;
    }


    public int getAge() {
        return this.age;
    }

    public String getGender() {
        return this.gender;
    }

    public void show() {
        System.out.println("学生姓名：" + this.name + "，年龄：" + this.age + "，性别：" + this.gender + "，老师：" + teacherName);
    }

    public void study() {
        System.out.println(this.name + "正在学习");
    }
}
