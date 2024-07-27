# Java 循环进阶案例

## 案例一

```java
/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 12:54:11 UTC+08:00
 *****************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class Demo01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("请输入第" + (i + 1) + "个班的成绩");
            double sum = 0;
            for (int j = 0; j < 4; j++) {
                System.out.print("请输入第" + (j + 1) + "个学生的成绩: ");
                double score = scanner.nextDouble();
                sum += score;
            }
            System.out.println("第" + (i + 1) + "班的平均分为: " + sum / 4);
            System.out.println("=".repeat(50));

        }

    }
}

```

