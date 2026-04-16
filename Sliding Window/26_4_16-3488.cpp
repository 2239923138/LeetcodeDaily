/*
3488. 距离最小相等元素查询
给你一个 环形 数组 nums 和一个数组 queries 。

对于每个查询 i ，你需要找到以下内容：

数组 nums 中下标 queries[i] 处的元素与 任意 其他下标 j（满足 nums[j] == nums[queries[i]]）之间的 最小 距离。如果不存在这样的下标 j，则该查询的结果为 -1 。
返回一个数组 answer，其大小与 queries 相同，其中 answer[i] 表示查询i的结果。

1 <= queries.length <= nums.length <= 105
1 <= nums[i] <= 106
0 <= queries[i] < nums.length
*/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> solveQueries(vector<int> &nums, vector<int> &queries)
    {
        unordered_map<int, vector<int>> mp;
        int sz = nums.size();
        for (size_t i = 0; i < sz; i++)
        {
            mp[nums[i]].push_back(i);
        }
        for (auto &[_, p] : mp)
        {
            int i0 = p[0];
            p.insert(p.begin(), p.back() - sz);
            p.push_back(i0 + sz);
        }

        for (int &i : queries)
        {
            auto &p = mp[nums[i]];
            if (p.size() == 3)
            {
                i = -1;
            }
            else
            {
                int j = ranges::lower_bound(p, i) - p.begin();
                i = min(i - p[j - 1], p[j + 1] - i);
            }
        }
        return queries;
    }
};