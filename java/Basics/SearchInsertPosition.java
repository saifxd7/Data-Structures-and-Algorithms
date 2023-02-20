public class SearchInsertPosition {
    public static void main(String[] args) {
        int[] srchArray = {1,3,5,6};
        int target = 5;
        System.out.print(searchInsert(srchArray, target));
    }

    public static int searchInsert(int[] nums, int target) {
        int i;
        for(i = 0; i < nums.length; i++)
            if(nums[i] >= target)
                return i;   
        return i;
    }
}
