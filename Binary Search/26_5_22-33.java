class Solution {
    public int search(int[] nums, int target) {
        int sz = nums.length;
        int left = -1, right = sz;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            int x = nums[mid];
            if (target > nums[sz - 1] && nums[sz - 1] >= x) {
                right = mid;
            } else if (x > nums[sz - 1] && nums[sz - 1] >= target) {
                left = mid;
            } else if (x >= target) {
                right = mid;
            } else {
                left = mid;

            }
        }
        return nums[right] == target ? right : -1;
    }
}