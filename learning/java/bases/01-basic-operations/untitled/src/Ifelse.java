/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-20 13:33:02 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class Ifelse {
    public static void main(String[] args) {
        boolean flag = true;
        if (flag) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
        
        int score = 70;
        if (score >= 90) {
            System.out.println("优秀");
        } else if (score >= 70 && score < 90) {
            System.out.println("良好");
        } else if (score >= 60 && score < 70) {
            System.out.println("一般");
        } else {
            System.out.println("较差");
        }
        
        
        
    }
}
