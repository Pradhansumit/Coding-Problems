#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> productQueries(int n, const vector<vector<int>> &queries)
    {
        vector<int> powers;
        int sum = 0, i = 0;
        // while(sum < n){
        //     int curr = 1LL << i;
        //     if(curr == n){
        //         powers.clear();
        //         powers.push_back(curr);
        //         break;
        //     }
        //     else{
        //         sum += curr;
        //         powers.push_back(curr);
        //     }
        //     i++;
        // }

        for (int i = 0; i < 32; i++)
        {
            if ((n & (1 << i)) != 0)
            {
                powers.push_back(1 << i);
            }
        }

        vector<int> res;

        for (int i = 0; i < queries.size(); i++)
        {
            int product = 1;
            for (int j = queries[i][0]; j < queries[i][1] + 1; j++)
            {
                product *= powers[j];
            }
            res.push_back(product);
        }

        for (auto x : res)
        {
            cout << x << " ";
        }
        cout << "\n";

        return {};
    }
};

int main()
{
    Solution sol;
    sol.productQueries(15, {{0, 1}, {2, 2}, {0, 3}});
    return 0;
}
