/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-31 22:53:30 UTC+08:00
 ****************************************************/
package host.fairy.students;

import java.util.ArrayList;

/**
 * @author Lionel Johnson
 */
public class StudentsService {
    static ArrayList<Student> students = new ArrayList<>();

    public boolean addStudent(Student student) {
        if (!students.isEmpty()) {
            for (Student s : students) {
                if (s.id == student.id) {
                    System.out.println("学号已存在，请重新输入！");
                    return false;
                }
            }
        }
        students.add(student);
        return true;
    }

    public boolean deleteStudent(int id) {
        if (students.isEmpty()) {
            System.out.println("学生列表为空！");
            return false;
        }
        for (Student s : students) {
            if (s.id == id) {
                students.remove(s);
                return true;
            }
        }
        System.out.println("学号不存在！");
        return false;
    }

    public boolean modifyStudent(Student student) {
        if (students.isEmpty()) {
            System.out.println("学生列表为空！");
            return false;
        }
        for (Student s : students) {
            if (s.id == student.id) {
                s.name = student.name;
                s.age = student.age;
                s.address = student.address;
                return true;
            }
        }
        System.out.println("学号不存在！");
        return false;
    }

    public void queryStudent(int id) {
        if (students.isEmpty()) {
            System.out.println("学生列表为空！");
            return;
        }
        for (Student s : students) {
            if (s.id == id) {
                System.out.println("学号\t姓名\t年龄\t家庭住址");
                System.out.println(s.id + "\t" + s.name + "\t" + s.age + "\t" + s.address);
                return;
            }
        }
        System.out.println("学号不存在！");
    }
}
