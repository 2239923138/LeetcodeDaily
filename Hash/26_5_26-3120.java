package Hash;

import java.util.HashSet;

class Solution {
    public int numberOfSpecialChars(String word) {
        // A-Z 65-90 a-z 97-122
        int ans = 0;
        HashSet<Integer> upper = new HashSet<>();
        HashSet<Integer> lower = new HashSet<>();

        for (int i = 0; i < word.length(); i++) {
            int n = word.charAt(i);
            if (n >= 65 && n <= 90) {
                if (!upper.contains(n) && lower.contains(n + 32)) {
                    ans++;
                }
                upper.add(n);
            } else {
                if (!lower.contains(n) && upper.contains(n - 32)) {
                    ans++;
                }
                lower.add(n);
            }
        }
        return ans;
    }
}