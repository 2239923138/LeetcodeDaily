/*
3783. 整数的镜像距离
给你一个整数 n。

定义它的 镜像距离 为：abs(n - reverse(n))​​​​​​​，其中 reverse(n) 表示将 n 的数字反转后形成的整数。

返回表示 n 的镜像距离的整数。

其中，abs(x) 表示 x 的绝对值。

1 <= n <= 109
*/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int mirrorDistance(int n)
    {
        int rev = 0, m = n;
        for (; m > 0; m /= 10)
        {
            rev *= 10;
            rev += m % 10;
        }
        return n - rev < 0 ? rev - n : n - rev;
    }
};