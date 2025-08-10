#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    bool reorderedPowerOf2(int n){
        string s = to_string(n);
        sort(s.begin(), s.end());
        for(int i = 0; i < 32; i++){
            long long val = 1LL << i;
            string s_val = to_string(val);
            sort(s_val.begin(), s_val.end());
            if(s_val == s){
                return true;
            }
        }
        return false;
    };
};