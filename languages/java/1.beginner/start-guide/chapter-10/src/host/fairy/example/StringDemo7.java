/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 20:16:56 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class StringDemo7 {
    public static String encryptPhoneNumber(String phoneNumber) {
        StringBuilder stringBuilder = new StringBuilder();
        String startString = phoneNumber.substring(0, 3);
        String endString = phoneNumber.substring(7);
        return stringBuilder.append(startString).append("****").append(endString).toString();
    }
    
    public static String encryptCardNumber(String cardNumber) {
        StringBuilder stringBuilder = new StringBuilder();
        String startString = cardNumber.substring(0, 4);
        String endString = cardNumber.substring(12);
        return stringBuilder.append(startString).append("************").append(endString).toString();
    }
    
    public static String encryptBlack(String blackString) {
        return blackString.replace("TMD", "***");
    }
    
    public static void main(String[] args) {
        String phoneNumber = "13312345678";
        System.out.println("Encrypted phone number: " + encryptPhoneNumber(phoneNumber));
        
        String cardNumber = "6222020202020202020";
        System.out.println("Encrypted card number: " + encryptCardNumber(cardNumber));
        
        String blackString = "TMD, I'm so angry!";
        System.out.println("Encrypted black string: " + encryptBlack(blackString));
    }
}
