#include <stdio.h>

int main() {
    int arr[3][4];
    int (*p)[4] = arr;

    printf("%p\n", p);
}
