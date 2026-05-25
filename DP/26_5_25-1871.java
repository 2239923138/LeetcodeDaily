class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        int[] f = new int[n];
        int[] sum = new int[n + 1];
        f[0] = 1;
        sum[1] = 1;

        for (int j = 1; j < n; j++) {
            if (j >= minJump && s.charAt(j) == '0' && sum[j - minJump + 1] > sum[Math.max(j - maxJump, 0)]) {
                f[j] = 1;
            }
            sum[j + 1] = sum[j] + f[j];
        }
        return f[n - 1] == 1;
    }
}