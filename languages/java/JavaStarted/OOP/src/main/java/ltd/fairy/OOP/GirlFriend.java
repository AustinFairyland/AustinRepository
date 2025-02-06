/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 00:11:55 UTC+08:00
 *****************************************************/
package ltd.fairy.OOP;

/**
 * @author Lionel Johnson
 */
public class GirlFriend {

    String name;
    int age;
    String gender;

    private GirlFriend() {
    }

    public GirlFriend(String name, int age, String gender) {
        this.name = name;
        this.gender = gender;
        
        this.assignAge(age);
    }

    private void assignAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("年龄不能为负数");
        } else if (age > 120) {
            throw new IllegalArgumentException("年龄不能超过120岁");
        } else {
            this.age = age;
        }
    }


    public void sleep() {
        System.out.println(this.name + "正在睡觉...");
    }


}
