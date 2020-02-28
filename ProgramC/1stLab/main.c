#include <stdio.h>
#include <malloc.h>
#include <time.h>

void input(int* n, int* klu, int** dummy)
{
    int* arr;
    int size = 0, k = 0;

    for (;;)
    {
        if (size == 0)
        {
            printf("How many elements will array be?\n");
            scanf("%d", &size);
            if (size <= 0)
            {
                printf("Your array can't have negative elements\n");
                size = 0;
                continue;
            }
        }
        break;
    }

    for (;;) {
        if (k == 0) {
            printf("What is k?\n");
            scanf("%d", &k);
            if (k <= 0) {
                printf("Make it positive\n");
                k = 0;
                continue;
            }
        }
        break;
    }

    int fill = 0;
    printf("How do you want to fill the array?\n1. Random\n2. Manual\n");
    for (;;) {
        scanf("%d", &fill);
        if (fill != 1 && fill != 2){
            printf("No such option\n");
            continue;
        }
        break;
    }

    arr = calloc(size, sizeof(int));
    *klu = k;
    *n = size;
    srand(time(NULL));

    for (int i = 0; i < size; i++)
    {
        if (fill == 2) {
            printf("\nElement %d:  ", i + 1);
            scanf("%d", &arr[i]);
        }
        else if (fill == 1){
            arr[i] = rand() % 20;
        }
    }
    *dummy = arr;
}

int comp(const void * elem1, const void * elem2)
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

static void calculate(int** arr, int** res, int* size, int* k){
    int *source, *sorted, *clusters = NULL;
    source = sorted = clusters = calloc(*size, sizeof(int));

    int clust = 1;
    for (int i = 0; i < *size; i++){
        clusters[i] = 0;
        sorted[i] = arr[i];
        source[i] = arr[i];
    }
    qsort(sorted, *size, sizeof(int), comp);

    for (int i = 0; i < *size; i++){
        if (sorted[0] == source[i]){
            clusters[i] = 1;
        }
    }

    for (int i = 1; i < *size; i++){
        if (sorted[i] == sorted[i-1]) continue;
        else if (sorted[i] - sorted[i-1] < *k){
            ;
        }
        else if (sorted[i] - sorted[i-1] >= *k){
            clust += 1;
        }
        for (int n = 0; n < *size; n++) {
            if (sorted[i] == source[n]) {
                clusters[n] = clust;
            }
        }
    }
    *res = clusters;

    for (int loop = 0; loop < *size; loop++)
    {
        printf("%d ", source[loop]);
    }
    printf("] - source\n");
    for (int loop = 0; loop < *size; loop++)
    {
        printf("%d ", clusters[loop]);
    }
    printf("] - clusters\n");
    for (int loop = 0; loop < *size; loop++)
    {
        printf("%d ", sorted[loop]);
    }
    printf("] - sorted\n");
}


int main() {
    printf("Hello, World!\n");
    int c;
    int *src = NULL, *result = NULL;
    int n = 0, k = 0;
    for (;;)
    {
        printf("Whatcha want?\n1. Enter array\n2. Proceed array\n3. Output array\n4. Exit\n");
        scanf("%d", &c);

        if (c == 1)
        {
            input(&n, &k, &src);
            result = NULL;
        }
        else if(c == 2)
        {
            calculate(&src, &result, &n, &k);
        }
        else if(c == 3)
        {
            printf("[");
            for (int loop = 0; loop < n; loop++)
            {
                printf("%d ", src[loop]);
            }
            printf("] - source\n");

            if (result == NULL) {
                printf("Not proceeded yet\n");
            }
            else {
            printf("[");
            for (int loop = 0; loop < n; loop++)
            {
                printf("%d ", result[loop]);
            }
            printf("]\n");
            }
        }
        else if(c == 4)
        {
            break;
        }
    }
    return 0;
}
