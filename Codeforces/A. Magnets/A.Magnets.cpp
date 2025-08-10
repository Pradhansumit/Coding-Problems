#include <bits/stdc++.h>
using namespace std;

/*
Using Stack

int main(){
    int n; cin >> n;
    stack<int> st;
    int res = 1;
    for(int i = 0; i < n; i++){
        int x; cin >> x;
        if(st.size() and st.top() != x){
            res++;
        }
        st.push(x);
    }
    cout << res << "\n";
    return 0;
}
*/

int main()
{
    int n;
    cin >> n;
    string prev, curr;
    cin >> prev;
    int res = 1;
    for (int i = 1; i < n; i++)
    {
        cin >> curr;
        if (curr != prev) res++;
        prev = curr;
    }
    cout << res << "\n";
    return 0;
}