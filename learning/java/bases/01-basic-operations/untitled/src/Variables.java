/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-19 21:45:06 UTC+08:00
 ******************************************************/

/**
 * @author Lionel Johnson
 */
public class Variables {
    /**
     * 变量命名规范:<br>
     * 字符一般为英文字符<br>
     * 1. 首字母必须是以 字符, $, _ 开头<br>
     * 2. 结尾: 字符, $, _, 数字(0-9)<br>
     * 3. 保留字不可用<br>
     *
     * @param args null
     */
    public static void main(String[] args) {

        String str = "=".repeat(50);

        // 示例
        System.out.println(str);
        final int adultAge = 18;  // 加上 `final` 关键字就是常量而不是变量
        System.out.println("常量 adultAge:" + adultAge);
        int age = 18;  // 声明变量 age 为 int 类型 初始化赋值18
        System.out.println("声明变量并初始化 -> 年龄:" + age);
        age = 28;  // 修改变量的值
        System.out.println("变量重新赋值 -> 年龄:" + age);

        // 常用的数据类型
        System.out.println(str);
        byte byteInteger = 127;  // 整型, 8位, 有符号的, 以二进制补码表示的整数, 范围: -128 ~ 127
        short shortInteger = 32767;  // 整型, 16位, 范围: -32768 ~ 32767
        int intInteger = 10;  // 整型, 32位, 占用 4字节, 范围: -2147483648 ~ 2147483647
        long longInteger = 10;  // 整型, 32位, 占用 4字节, 范围: -2147483648 ~ 2147483647
        float floatFloat = 123.555f;  // 单精度浮点型, 32位
        double doubleFloat = 3.14;  // double 双精度浮点型, 浮点数的默认类型为`double`类型, 占用8字节, 15 decimal, 默认值是0.0d
        boolean boolBoolean = true;  // boolean 
        char charChar = 97;  // char 字符型
        String strString = "中国";  // 字符串

        System.out.println("8位整型: " + byteInteger);
        System.out.println("16位整型: " + shortInteger);
        System.out.println("32整数: " + intInteger);
        System.out.println("64整数: " + longInteger);
        System.out.println("32单精度浮点型: " + floatFloat);
        System.out.println("64双精度浮点型: " + doubleFloat);
        System.out.println("布尔型: " + boolBoolean);
        System.out.println("字符型: " + charChar);
        System.out.println("字符串: " + strString);

        System.out.println(str);
        // byte
        System.out.println("基本类型：byte 二进制位数：" + Byte.SIZE);
        System.out.println("包装类：java.lang.Byte");
        System.out.println("最小值：Byte.MIN_VALUE=" + Byte.MIN_VALUE);
        System.out.println("最大值：Byte.MAX_VALUE=" + Byte.MAX_VALUE);
        System.out.println(str);

        // short
        System.out.println("基本类型：short 二进制位数：" + Short.SIZE);
        System.out.println("包装类：java.lang.Short");
        System.out.println("最小值：Short.MIN_VALUE=" + Short.MIN_VALUE);
        System.out.println("最大值：Short.MAX_VALUE=" + Short.MAX_VALUE);
        System.out.println(str);

        // int
        System.out.println("基本类型：int 二进制位数：" + Integer.SIZE);
        System.out.println("包装类：java.lang.Integer");
        System.out.println("最小值：Integer.MIN_VALUE=" + Integer.MIN_VALUE);
        System.out.println("最大值：Integer.MAX_VALUE=" + Integer.MAX_VALUE);
        System.out.println(str);

        // long
        System.out.println("基本类型：long 二进制位数：" + Long.SIZE);
        System.out.println("包装类：java.lang.Long");
        System.out.println("最小值：Long.MIN_VALUE=" + Long.MIN_VALUE);
        System.out.println("最大值：Long.MAX_VALUE=" + Long.MAX_VALUE);
        System.out.println(str);

        // float
        System.out.println("基本类型：float 二进制位数：" + Float.SIZE);
        System.out.println("包装类：java.lang.Float");
        System.out.println("最小值：Float.MIN_VALUE=" + Float.MIN_VALUE);
        System.out.println("最大值：Float.MAX_VALUE=" + Float.MAX_VALUE);
        System.out.println(str);

        // double
        System.out.println("基本类型：double 二进制位数：" + Double.SIZE);
        System.out.println("包装类：java.lang.Double");
        System.out.println("最小值：Double.MIN_VALUE=" + Double.MIN_VALUE);
        System.out.println("最大值：Double.MAX_VALUE=" + Double.MAX_VALUE);
        System.out.println(str);

        // char
        System.out.println("基本类型：char 二进制位数：" + Character.SIZE);
        System.out.println("包装类：java.lang.Character");
        // 以数值形式而不是字符形式将Character.MIN_VALUE输出到控制台
        System.out.println("最小值：Character.MIN_VALUE=" + (int) Character.MIN_VALUE);
        // 以数值形式而不是字符形式将Character.MAX_VALUE输出到控制台
        System.out.println("最大值：Character.MAX_VALUE=" + (int) Character.MAX_VALUE);

        // 常量, 前面加关键字 `final`, 全部大写
        System.out.println(str);
        final int ADULTAGE = 18;
        System.out.println(ADULTAGE);
        final String CHINA = "中国";
        System.out.println(CHINA);
    }
}
