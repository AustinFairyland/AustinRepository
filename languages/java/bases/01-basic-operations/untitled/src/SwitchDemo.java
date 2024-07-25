/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-21 01:59:07 UTC+8
 ******************************************************/

/**
 * @author Lionel Johnson
 */
public class SwitchDemo {
    public static void main(String[] args) {
        int ranking = 1;

        switch (ranking) {
            case 1:
                System.out.println("第一名");
                break;
            case 2:
                System.out.println("第二名");
                break;
            case 3:
                System.out.println("第三名");
                break;
            default:
                System.out.println("没有..");
                break;

        }
    }
}