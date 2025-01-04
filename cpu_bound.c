#include "cpu_bound.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <math.h>
#include <pthread.h>
#include <sys/wait.h>


// File Operations
int process_yob(FILE* f) {
    
}


// Matrix Operations       Basic Tests: OK       Intermediate Tests: ___       Simulation: ___
void mat_add(int len, int wid, int* mat1, int* mat2, int* res) {
    for (int i = 0; i < len * wid; i++)
        res[i] = mat1[i] + mat2[i];
}

void mat_sub(int len, int wid, int* mat1, int* mat2, int* res) {
    for (int i = 0; i < len * wid; i++)
        res[i] = mat1[i] - mat2[i];
}

void mat_mul(int len, int wid1, int wid2, int mat1[len][wid1], int mat2[wid1][wid2], int res[len][wid2]) {
    int sum;
    for (int i = 0; i < wid2; i++) {
        for (int j = 0; j < len; j++) {
            sum = 0;
            for (int k = 0; k < wid1; k++) {
                sum += mat1[j][k] * mat2[k][i];
            }
            res[j][i] = sum;
        }
    }
}


// Prime Generation       Basic Tests: OK       Intermediate Tests: ___       Simulation: ___
static int is_prime(int n) {
    if (n == 1)
        return 0;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0) return 0;
    return 1;
}

int primes(int** ret, int start, int end) {
    int* buff = malloc(50 * sizeof(int));
    if (buff == NULL)
        perror("__primes: Initial allocation failed");

    int size = 50;
    int occ = 0;

    for (int i = start; i <= end; i++) {
        if (is_prime(i)) {
            if (occ == size) {
                buff = realloc(buff, sizeof(int) * (size + 20));
                if (buff == NULL)
                    perror("__primes: Realloc failed");
                size += 20;
            }
            buff[occ] = i;
            occ++;
        }
    }

    *ret = buff;
    return occ;
}


int main() {
    
}
