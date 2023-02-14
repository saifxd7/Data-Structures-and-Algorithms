public class SquareRootWithoutBuiltInFunction {
    public static void main(String[] args) {
        System.out.print(SqrtOf(64));
    }

    public static int SqrtOf(int num) {
        // Using Binary Search Approach
        int start = 0;
        int end = num;
        while(start<=end) {
            int mid = start + (end-start)/2;
            if(mid*mid==num) {
                return mid;
            }
            else if(mid*mid<num) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return 0;
    }
}
