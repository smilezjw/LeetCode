public class LemonadeChange {
    public boolean lemonadeChange(int[] bills) {
        if (bills != null && bills.length == 0) {
            return true;
        }
        int fiveCnt = 0, tenCnt = 0;
        for (int i = 0; i < bills.length; i++) {
            if (bills[i] == 5) {
                fiveCnt++;
            } else if (bills[i] == 10) {
                if (fiveCnt <= 0) {
                    return false;
                }
                fiveCnt--;
                tenCnt++;
            } else {
                if (fiveCnt > 0 && tenCnt > 0) {
                    fiveCnt--;
                    tenCnt--;
                } else if (fiveCnt >= 3) {
                    fiveCnt -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
