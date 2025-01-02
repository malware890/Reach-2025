#include "thd_algos.h"
#include <stdio.h>
#include <pthread.h>
#include <sys/wait.h>

int process_yob(FILE* f) {
    
}

void mat_add(int len, int wid, int mat1[len][wid], int mat2[len][wid], int res[len][wid]) {
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < wid; j++)
            res[i][j] = mat1[i][j] + mat2[i][j];
    }
}

void mat_sub(int len, int wid, int mat1[len][wid], int mat2[len][wid], int res[len][wid]) {
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < wid; j++)
            res[i][j] = mat1[i][j] - mat2[i][j];
    }
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

int main() {
    int m1[2][2] = {
        {2, 1},
        {1, 4},
    };

    int m2[2][3] = {
        {1, 2, 0},
        {0, 1, 2}
    };

    int m3[2][3];

    mat_mul(2, 2, 3, m1, m2, m3);
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++)
            printf("%d ", m3[i][j]);
        printf("\n");
    }

}
