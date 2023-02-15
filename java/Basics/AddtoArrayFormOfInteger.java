import java.util.*;;

class AddtoArrayFormOfInteger {
    
    // Input: num = [1,2,0,0], k = 34
    // Output: [1,2,3,4]
    // Explanation: 1200 + 34 = 1234

    public static void main(String[] args) {
        int[] num = { 1,2,0,0 };
        int k = 34;
        List<Integer> returnedList = addToArrayForm_Optimized(num, k);
        for(int i : returnedList) {
            System.out.print(i);
        }
    }

    // BrutForce Approch
    public static List<Integer> addToArrayForm_BrutForce(int[] num, int k) {
        String str = "";
        for(int i=0; i<num.length; i++) {
            str = str + num[i];
        }
        int num1 = Integer.parseInt(str);
        int rtnMainInt = num1 + k;
        String strInt = Integer.toString(rtnMainInt);
        int[] newGuess = new int[strInt.length()];
        for (int i = 0; i < strInt.length(); i++)
        {
            newGuess[i] = strInt.charAt(i) - '0';
        }
        List<Integer> intList = new ArrayList<Integer>(newGuess.length);
        for (int i : newGuess)
        {
            intList.add(i);
        }
        return intList;
    }

    // Optimized Approach
    public static List<Integer> addToArrayForm_Optimized(int[] num, int k) {
        LinkedList<Integer> res=new LinkedList<>();
        int len=num.length-1;
        while(len>=0 || k>0){
            if(len>=0){
                k+=num[len--];
            }
            res.addFirst(k%10);
            k/=10;
        }
        return res;
    }
}