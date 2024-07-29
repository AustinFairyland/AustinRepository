/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 01:36:44 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class MoneyToChinese {

    private static final String[] CN_NUMBERS = {"零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"};
    private static final String[] CN_UNITS = {"", "拾", "佰", "仟"};
    private static final String[] CN_BIG_UNITS = {"", "万", "亿"};
    private static final String CN_INTEGER = "整";
    private static final String CN_YUAN = "元";
    private static final String CN_JIAO = "角";
    private static final String CN_FEN = "分";

    public static String convert(double amount) {
        if (amount < 0 || amount > 9999999999999.99) {
            throw new IllegalArgumentException("金额超出范围");
        }

        long integerPart = (long) amount;
        int fractionPart = (int) Math.round((amount - integerPart) * 100);

        String integerPartStr = convertIntegerPart(integerPart);
        String fractionPartStr = convertFractionPart(fractionPart);

        if (fractionPart == 0) {
            return integerPartStr + CN_YUAN + CN_INTEGER;
        } else {
            return integerPartStr + CN_YUAN + fractionPartStr;
        }
    }

    private static String convertIntegerPart(long integerPart) {
        if (integerPart == 0) {
            return CN_NUMBERS[0];
        }

        StringBuilder result = new StringBuilder();
        int unitPos = 0;
        boolean zero = false;

        while (integerPart > 0) {
            int segment = (int) (integerPart % 10000);
            if (segment == 0) {
                if (!zero) {
                    result.insert(0, CN_NUMBERS[0]);
                    zero = true;
                }
            } else {
                String segmentStr = convertSegment(segment);
                result.insert(0, segmentStr + CN_BIG_UNITS[unitPos]);
                zero = false;
            }
            integerPart /= 10000;
            unitPos++;
        }

        return result.toString();
    }

    private static String convertSegment(int segment) {
        StringBuilder segmentStr = new StringBuilder();
        int unitPos = 0;
        boolean zero = false;

        while (segment > 0) {
            int digit = segment % 10;
            if (digit == 0) {
                if (!zero) {
                    segmentStr.insert(0, CN_NUMBERS[0]);
                    zero = true;
                }
            } else {
                segmentStr.insert(0, CN_NUMBERS[digit] + CN_UNITS[unitPos]);
                zero = false;
            }
            segment /= 10;
            unitPos++;
        }

        return segmentStr.toString();
    }

    private static String convertFractionPart(int fractionPart) {
        int jiao = fractionPart / 10;
        int fen = fractionPart % 10;

        StringBuilder result = new StringBuilder();
        if (jiao > 0) {
            result.append(CN_NUMBERS[jiao]).append(CN_JIAO);
        }
        if (fen > 0) {
            result.append(CN_NUMBERS[fen]).append(CN_FEN);
        }

        return result.toString();
    }
}
