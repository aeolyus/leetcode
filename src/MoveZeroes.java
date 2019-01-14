public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        int z = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                z++;
            } else {
                nums[i - z] = nums[i];
            }
        }
        for (int i = nums.length - z; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
