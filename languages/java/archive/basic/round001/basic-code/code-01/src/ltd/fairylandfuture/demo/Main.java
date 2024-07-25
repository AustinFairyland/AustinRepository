package ltd.fairylandfuture.demo;

public class Main {
    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("输入一个三位数值: ");
//        int number = sc.nextInt();
//
//        int ge = number % 10;
//        int shi = number / 10 % 10;
//        int bai = number / 100 % 10;
//
//        System.out.printf("个位是: %s\n", ge);
//        System.out.printf("十位是: %s\n", shi);
//        System.out.printf("百位是: %s\n", bai);

        String t1 = test1(10);
        System.out.println(t1);

    }

    public static String test1(int a) {
        if (a >= 10) {
            return "可以的";
        } else {
            return "不可以";
        }
    }

    public static String test2(boolean lightGreen , boolean lightYellow, boolean lightRed) {
        if (lightGreen) {
            return "GOGOGO";
        }
        if (lightYellow) {
            return "GO";
        }
        if (lightRed) {
            return "Stop";
        }


        return "";
    }

}
