/*
3761. 镜像对之间最小绝对距离

给你一个整数数组 nums。

镜像对 是指一对满足下述条件的下标 (i, j)：

0 <= i < j < nums.length，并且
reverse(nums[i]) == nums[j]，其中 reverse(x) 表示将整数 x 的数字反转后形成的整数。反转后会忽略前导零，例如 reverse(120) = 21。
返回任意镜像对的下标之间的 最小绝对距离。下标 i 和 j 之间的绝对距离为 abs(i - j)。

如果不存在镜像对，返回 -1。

1 <= nums.length <= 105
1 <= nums[i] <= 109
*/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int minMirrorPairDistance(vector<int> &nums)
    {
        unordered_map<int, int> mp;
        int n = nums.size(), ans = n;

        for (int j = 0; j < n; j++)
        {
            int x = nums[j];

            auto it = mp.find(x);
            if (it != mp.end())
            {
                ans = min(ans, j - it->second);
            }
            int rev = 0;
            for (; x > 0; x /= 10)
            {
                rev = rev * 10 + x % 10;
            }
            mp[rev] = j;
        }
        return ans < n ? ans : -1;
    }
};