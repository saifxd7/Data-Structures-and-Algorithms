public class XOROperationInArray {

    public static void main(String[] args) {
        // Input: n = 5, start = 0
        // Output: 8
        // Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
        // Where "^" corresponds to bitwise XOR operator.  
        System.out.print(xorOperation(5, 0));
    }

    public static int xorOperation(int n, int start) {
        int nums[] = new int[n];
        int bitwise = 0;
        for(int i=0; i<nums.length; i++) {
            nums[i] = start+2*i;
            bitwise = bitwise^nums[i];
        }
        return bitwise;
    }
}
