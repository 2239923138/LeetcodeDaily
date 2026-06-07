#include <bits/stdc++.h>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    TreeNode *createBinaryTree(vector<vector<int>> &descriptions)
    {
        int n = descriptions.size();
        unordered_map<int, TreeNode *> nodes;
        nodes.reserve(n + 1);
        unordered_set<int> children;
        children.reserve(n);

        for (const auto &d : descriptions)
        {
            int x = d[0], y = d[1];
            if (nodes.find(x) == nodes.end())
            {
                nodes[x] = new TreeNode(x);
            }
            if (!nodes.contains(y))
            {
                nodes[y] = new TreeNode(y);
            }
            if (d[2])
            {
                nodes[x]->left = nodes[y];
            }
            else
            {
                nodes[x]->right = nodes[y];
            }
            children.insert(y);
        }
        for (const auto &[x, node] : nodes)
        {
            if (children.find(x) == children.end())
            {
                return node;
            }
        }

        throw invalid_argument("Wrong");
    }
};