/*
2078. 两栋颜色不同且距离最远的房子

街上有 n 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 0 开始且长度为 n 的整数数组 colors ，其中 colors[i] 表示第  i 栋房子的颜色。

返回 两栋 颜色 不同 房子之间的 最大 距离。

第 i 栋房子和第 j 栋房子之间的距离是 abs(i - j) ，其中 abs(x) 是 x 的绝对值。

n == colors.length
2 <= n <= 100
0 <= colors[i] <= 100
生成的测试数据满足 至少 存在 2 栋颜色不同的房子
*/

/*
原先使用递归暴力求解，后完善思路改为O(N)解法
Python:
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        @cache
        def dfs(i,j):
            nonlocal colors
            if colors[i]!=colors[j]:
                return j-i
            if i+1==j:
                return 0
            return max(dfs(i+1,j),dfs(i,j-1))
        return dfs(0,len(colors)-1)
*/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxDistance(vector<int> &colors)
    {
        int n = colors.size();
        int c = colors[0];
        if (c != colors[n - 1])
        {
            return n - 1;
        }
        int r = n - 2;
        while (colors[r] == c)
        {
            r--;
        }
        int l = 1;
        while (colors[l] == c)
        {
            l++;
        }

        return max(r, n - 1 - l);
    }
};