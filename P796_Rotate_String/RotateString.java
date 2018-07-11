public class RotateString {
    public boolean rotateString(String A, String B) {
        if (A.length() != B.length()) {
            return false;
        }
        String doubleStr = A + A;
        return doubleStr.contains(B);
    }

    public static void main (String[] args) {

    }
}