/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 23:05:45 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.ArrayList;

/**
 * @author Lionel Johnson
 */
public class ArrayListDemo4 {
    public static boolean userExists(ArrayList<User> userArrayList, int id) {
        for (User u : userArrayList) {
            if (u.id == id) {
                return true;
            }
        }
        return false;
    }
    
    public static int getUserIndex(ArrayList<User> userArrayList, int id) {
        for (int i = 0; i < userArrayList.size(); i++) {
            if (userArrayList.get(i).id == id) {
                return i;
            }
        }
        return -1;
    }
    
    public static void main(String[] args) {
        ArrayList<User> userArrayList = new ArrayList<>();
        userArrayList.add(new User(1, "admin", "admin"));
        userArrayList.add(new User(2, "root", "root"));
        userArrayList.add(new User(3, "user", "user"));

        System.out.println(userExists(userArrayList, 4));
        System.out.println(getUserIndex(userArrayList, 2));
    }
}


