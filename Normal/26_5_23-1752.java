class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        int head = nums[0];
        int end = nums[n - 1];

        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    if (nums[j] < nums[j - 1]) {
                        return false;
                    }
                }
                return head >= end ? true : false;

            }

        }
        return true;
    }
}