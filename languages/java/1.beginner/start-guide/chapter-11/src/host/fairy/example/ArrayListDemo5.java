/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 23:37:17 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.ArrayList;

/**
 * @author Lionel Johnson
 */
public class ArrayListDemo5 {
    public static String getPhoneInfo(ArrayList<Phone> phoneArrayList, double price) {
        ArrayList<Phone> tempPhoneList = new ArrayList<>();

        for (Phone phone : phoneArrayList) {
            if (phone.price < price) {
                tempPhoneList.add(phone);
            }
        }

        if (tempPhoneList.isEmpty()) {
            return "No phone found with price less than " + price;
        } else {
            StringBuilder stringBuilder = new StringBuilder();
            for (Phone phone : tempPhoneList) {
                stringBuilder.append("Brand: ").append(phone.brand).append(", Price: ").append(phone.price).append("\n");
            }
            return stringBuilder.toString();
        }
        

    }
    
    public static void main(String[] args) {
        ArrayList<Phone> phoneArrayList = new ArrayList<>();
        phoneArrayList.add(new Phone("Xiaomi", 1000));
        phoneArrayList.add(new Phone("Apple", 8000));
        phoneArrayList.add(new Phone("Hammer", 2999));

        System.out.println(getPhoneInfo(phoneArrayList, 3000));
    }
    
}
