#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    vector<int> arr(n);
    vector<int> res;
    
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    for(int i =1; i <=n; i++){
        auto it = find(arr.begin(), arr.end(), i);
        if(it != arr.end()){
            auto idx = distance(arr.begin(), it);
            res.push_back(idx+1);
        }
    }
    for(auto x: res){
        cout << x << " ";
    }
    


    
    
    return 0;
}