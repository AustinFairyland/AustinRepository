/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 01:27:50 UTC+08:00
 *****************************************************/
package ltd.fairy.extend;

import ltd.fairy.parent.Persion;

/**
 * @author Lionel Johnson
 */
public class Student extends Persion {
    String school;


    public Student(String name, int age, String school) {
        super(name, age);
        this.school = school;
    }

    public String getSchool() {
        return school;
    }

    public void study() {
        System.out.println(this.name + "正在学习");
    }

}
