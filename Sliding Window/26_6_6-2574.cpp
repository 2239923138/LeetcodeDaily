#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> leftRightDifference(vector<int> &nums)
    {
        vector<int> ans = {0};
        int all = 0, cur = 0, pre = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            int now = nums[i];
            all += now;
            cur = cur + now + pre;
            ans.push_back(cur);
            pre = now;
        }

        for (int &i : ans)
        {
            i = abs(i - all);
        }
        return ans;
    }
};