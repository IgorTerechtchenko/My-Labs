#include <cstdio>
#include <iostream>

using namespace std;

long long count = 0;

void merge(long arr[], long l, long m, long r) {
    long left_count = m - l + 1;
    long right_count = r - m;

    long L[left_count];
    for (long i = 0; i < left_count; i++) {
        L[i] = arr[l + i];
    }

    long R[right_count];
    for (long j = 0; j < right_count; j++) {
        R[j] = arr[m + 1 + j];
    }

    long i = 0;
    long j = 0;
    long k = l;
    while (i < left_count && j < right_count) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        }
        else {
            arr[k++] = R[j++];
            count += left_count - i;
        }
    }

    while (i < left_count) {
        arr[k++] = L[i++];
    }

    while (j < right_count) {
        arr[k++] = R[j++];
    }
}

void merge_sort(long arr[], long l, long r) {
    if (l < r) {
        long m = l + (r - l) / 2;

        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    long n;
    cin >> n;

    long m[n];
    for (long i = 0; i < n; i++)
        cin >> m[i];

    merge_sort(m, 0, n - 1);
    cout << count;
    cout << "\n";
    return 0;
}
