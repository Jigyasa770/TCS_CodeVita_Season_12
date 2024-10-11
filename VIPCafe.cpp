#include <bits/stdc++.h>
using namespace std;

int VipCafe(vector<int>& arr, int pos) {
    int in = -1;
    int maxi = -1;
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        if (maxi < arr[i]) {
            in = i;
            maxi = arr[i];
        }
    }
    if (in == pos) return 0;
    arr[in] = -1;

    for (int i = 0; i < in; i++) {
        if (arr[i] > 0) arr[i]++;
    }

    return 1 + VipCafe(arr, pos);
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (auto &i : arr) cin >> i;
    int k;
    cin >> k;
    k--;
    cout << 1 + VipCafe(arr, k);
    return 0;
}
