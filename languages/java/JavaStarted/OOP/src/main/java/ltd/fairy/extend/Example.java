/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 22:58:41 UTC+08:00
 *****************************************************/
package ltd.fairy.extend;

/**
 * @author Lionel Johnson
 */
public class Example {

    public static void main(String[] args) {
        Zi zi = new Zi();
        zi.show();
    }
}


class FU {
    String name = "FU";
}

class Zi extends FU {
    String name = "Zi";

    public void show() {
        String name = "Zi show";
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);
    }
}
