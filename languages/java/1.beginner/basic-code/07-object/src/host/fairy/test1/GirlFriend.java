/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-28 01:22:10 UTC+08:00
 *****************************************************/
package host.fairy.test1;

/**
 * @author Lionel Johnson
 */
public class GirlFriend {
    String name;
    private int age;
    boolean gender;

    public GirlFriend() {
    }

    public GirlFriend(String name, int age, boolean gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
    

    public void sleep() {
        System.out.println("Sleeping...");
    }

    public void eat() {
        System.out.println("Eating...");
    }
    
}
