#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// int main(){

//     string s; cin >> s;
//     string ns;
//     for(int i = s.length()-1; i > -1; i--){
//         ns += s[i];
//     }
//     cout << ns;
    
//     return 0;
// }

int main(){
    string s; cin >> s;
    reverse(s.begin(), s.end());
    cout << s;
    return 0;
}