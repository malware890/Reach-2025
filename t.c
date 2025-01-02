#include <stdio.h>

void fn(int arr[]) {
    printf("%lu", sizeof(arr));
}

int main() {
    int arr[3] = {1, 2, 3};
    fn(arr);
}
