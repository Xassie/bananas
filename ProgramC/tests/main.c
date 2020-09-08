#include <stdio.h>
#include <malloc.h>

int main() {
    int** arr = (int**)malloc(5 * sizeof(int*));
    for (int i = 0; i < 5; i++)
    {
        arr[i] = (int*)malloc(8 * sizeof(int));
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            arr[i][j] = i+j;
        }
    }

    int** copy = (int**)malloc(5 * sizeof(int*));
    for (int i = 0; i < 5; i++)
    {
        copy[i] = (int*)malloc(8 * sizeof(int));
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            copy[i][j] = arr[i][j];
        }
    }

    copy[2][5] = 1000;

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            printf("%d == %d\n", arr[i][j],  copy[i][j]);
        }
    }
    for (int i = 0; i < 5; i++)
    {
        free(arr[i]);
        free(copy[i]);
    }
    return 0;
}
