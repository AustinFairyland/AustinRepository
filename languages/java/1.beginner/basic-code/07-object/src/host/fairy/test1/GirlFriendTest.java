/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-28 01:23:50 UTC+08:00
 *****************************************************/
package host.fairy.test1;

/**
 * @author Lionel Johnson
 */
public class GirlFriendTest {
    public static void main(String[] args) {
        GirlFriend girlFriend = new GirlFriend("Alice", 20, false);

        System.out.println("Name: " + girlFriend.name);
        System.out.println("Age: " + girlFriend.getAge());
        System.out.println("Gender: " + (girlFriend.gender ? false : "女"));

        girlFriend.eat();
    }
}
