class Solution {
    public int triangularSum(int[] nums) {
       while (nums.length > 1) {
            int n = nums.length;
            List<Integer> newNums = new ArrayList<>();
            for (int i = 0; i < n - 1; i++) {
                newNums.add((nums[i] + nums[i + 1]) % 10);
            }
            nums = newNums.stream().mapToInt(Integer::intValue).toArray();
        }
        return nums[0];
        
    }
}