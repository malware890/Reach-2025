#pragma once

void mat_add(int len, int wid, int* mat1, int* mat2, int* res);
void mat_sub(int len, int wid, int* mat1, int* mat2, int* res);
// void mat_mul(int len, int wid1, int wid2, int mat1[len][wid1], int mat2[wid1][wid2], int res[len][wid2]);
static inline int is_prime(int n);
int primes(int** ret, int start, int end);
void solve_sys();
