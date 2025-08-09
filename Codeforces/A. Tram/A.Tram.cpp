
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int count = 0;
    int res = 0;
    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        count = count-a + b;
        res = max(res, count);
    }
    cout << res;
    return 0;
}
