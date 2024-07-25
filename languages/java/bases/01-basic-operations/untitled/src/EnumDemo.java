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
public class EnumDemo {
    // 使用枚举的实例
    Day day;

    // 构造函数
    public EnumDemo(Day day) {
        this.day = day;
    }

    // 方法
    public void dayIsLike() {
        switch (day) {
            case MONDAY:
                System.out.println("Mondays are bad.");
                break;

            case FRIDAY:
                System.out.println("Fridays are better.");
                break;

            case SATURDAY:
            case SUNDAY:
                System.out.println("Weekends are best.");
                break;

            default:
                System.out.println("Midweek days are so-so.");
                break;
        }
    }

    // 主函数
    public static void main(String[] args) {
        // 创建一个 Main 类的对象，并传递一个 Day 枚举的实例给它
        EnumDemo m1 = new EnumDemo(Day.MONDAY);
        m1.dayIsLike();
        EnumDemo m2 = new EnumDemo(Day.FRIDAY);
        m2.dayIsLike();
    }
}

