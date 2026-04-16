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