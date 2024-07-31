/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-08-01 01:10:35 UTC+08:00
 ****************************************************/
package host.fairy.a02static02;

/**
 * @author Lionel Johnson
 */
public class SubClass extends Parent {
    public static void staticMethod() {
        System.out.println("SubClass static method");
    }

    public void instanceMethod() {
        System.out.println("SubClass instance method");
    }

    public static void main(String[] args) {
        Parent parent = new SubClass();
        parent.instanceMethod();
    }
}
