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
public class Operators {
    /**
     * 运算符 <br>
     * 1. 赋值运算符 <br>
     * 加法: +=, 如果是 `+=1` 可以简化为 ++ <br>
     * 减法: -=, 如果是 `-=1` 可以简化为 -- <br>
     * 乘法: *= <br>
     * 除以: /= <br>
     * 取模: %= <br>
     * <br>
     * 2. 关系运算符(比较运算符) <br>
     * 结果是 boolean 类型 <br>
     * 大于: > <br>
     * 小于: < <br>
     * 等于: == <br>
     * 不等于: != <br>
     * 大于等于: >= <br>
     * 小于等于: <= <br>
     * <br>
     * 3. 与或非 <br>
     * 与: &&, 表示 and, 一个为假, 结果就是假 <br>
     * 或: ||, 表示 or, 一个为真, 结果为真 <br>
     * 非: !, 表示 not, 反 <br>
     *
     * @param args null
     */
    public static void main(String[] args) {
        // 赋值运算符
        int age = 18;
        System.out.println("初始化并赋值: age = " + age);
        age += 2;  // 把 age 原来的值加2在重新赋值给 age, 等价于 age = age + 2
        System.out.println("重新赋值并加2: age = " + age);
        age++;  // 把 age 原来的值加1, 等价于 age += 1; age = age + 1
        System.out.println("重新赋值并加1: age = " + age);
        // 取模
        int year1 = 2019;
        int year2 = 2020;
        year1 /= 4;
        System.out.println(year1);  // 504
        year1 = 2019;
        year1 %= 4;
        System.out.println(year1);  // 3

        year2 /= 4;
        System.out.println(year2);  // 505
        year2 = 2020;
        year2 %= 4;
        System.out.println(year2);  // 0

        // 关系运算符, 返回的都是 boolean 类型的数据, 即 true , false
        System.out.println(3 < 1);

        // 逻辑运算符, 参考 `Ifelse.java` 的示例

    }
}
