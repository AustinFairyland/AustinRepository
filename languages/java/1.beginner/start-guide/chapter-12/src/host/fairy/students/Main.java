/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-31 22:49:18 UTC+08:00
 ****************************************************/
package host.fairy.students;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
//        StudentsService studentsService = new StudentsService();

        boolean flag = true;
        while (flag) {
            System.out.println("-------------欢迎来到学生管理系统----------------");
            System.out.println("1：添加学生");
            System.out.println("2：删除学生");
            System.out.println("3：修改学生");
            System.out.println("4：查询学生");
            System.out.println("5：退出");
            System.out.print("请输入您的选择:");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    boolean addStatus = StudentsService.addStudent(new Student(1, "张三", 18, "北京"));
                    if (addStatus) {
                        System.out.println("添加成功！");
                    }
                    break;
                case 2:
                    System.out.println("删除学生");
                    break;
                case 3:
                    System.out.println("修改学生");
                    break;
                case 4:
                    StudentsService.queryStudent(1);
                    break;
                default:
                    flag = false;
                    break;
            }
        }
    }
}
