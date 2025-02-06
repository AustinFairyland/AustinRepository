/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 23:45:37 UTC+08:00
 *****************************************************/
package ltd.fairy.OOP;

/**
 * @author Lionel Johnson
 */
public class Phone {

    public String name;
    public String color;
    public double price;

    private void str() {
        System.out.println("品牌" + this.name + ", 颜色" + this.color + ", 价格" + this.price);
    }

    public String call(String name) {
        this.str();
        return "Calling " + name + "...";
    }

    public String sendMsg(String name, String msg) {
        this.str();
        return "Sending message to " + name + ": " + msg;
    }
}
