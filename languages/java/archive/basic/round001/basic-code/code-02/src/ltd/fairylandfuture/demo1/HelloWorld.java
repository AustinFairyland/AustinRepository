package ltd.fairylandfuture.demo1;


public class HelloWorld {
    public static void main(String[] args) {
        // 输出
        System.out.println("Hello World.");
        String a = "123";
        System.out.println(a);

        byte b = 10;
        short s = 20;
        long n = 100L;
//        long results = b + s + n;
//        System.out.println(results);

        String name = "name";
        String results = name + 123;
        System.out.println(results);

        int age = 18;
        System.out.println("我的年龄是" + age + "岁");
        System.out.printf(String.format("我的年龄是%s岁", age));

    }
}
