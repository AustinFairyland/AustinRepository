/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-08-03 18:35:24 UTC+08:00
 ****************************************************/
package host.fairy.extend;

/**
 * @author Lionel Johnson
 */
public class Test {
    // 变量作用域
    public static void main(String[] args) {
        Zi z = new Zi();
        z.show();
    }
}

class Fu {
    String name = "Fu";
}

class Zi extends Fu {
    String name = "Zi";

    public void show() {
        String name = "show";
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);
    }
}
