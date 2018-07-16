public class PeakIndexInAMountainArray {
    public int peakIndexInMountainArray(int[] A) {
        int low = 0;
        int high = A.length - 1;
        while (low < high) {
            int mid = (low + high) / 2;
            if (A[mid] < A[mid+1]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}
