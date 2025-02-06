/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 23:44:13 UTC+08:00
 *****************************************************/
package ltd.fairy;

import ltd.fairy.OOP.Phone;

/**
 * @author Lionel Johnson
 */
public class Main {
    public static void main(String[] args) {
        Phone phone = new Phone();
        phone.name = "iPhone 13";
        phone.color = "Blue";
        phone.price = 1399.00;
        
        System.out.println(phone.call("张山"));
    }
}
