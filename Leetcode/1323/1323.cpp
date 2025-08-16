#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maximum69Number(int num)
    {
        int pv = 0;   // placevalue
        int pvs = -1; // placevaluesix

        int n = num;
        while (n > 0)
        {
            int rem = n % 10;
            if (rem == 6)
            {
                pvs = pv;
            }
            n /= 10;
            pv++;
        }
        if (pvs == -1)
            return num;
        return num + 3 * pow(10, pvs);
    }
};