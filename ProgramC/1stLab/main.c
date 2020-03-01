#include <stdio.h>
#include <malloc.h>
#include <time.h>

int* input(int* n, int* klu) {
    // Function that catches user's input
    // and transfers it to the determined variables


    int *arr;
    int size = 0, k = 0;
    int const area = 30;

    // Asks the size of array
    for (;;) {
        if (size == 0) {
            printf("How many elements will array be?\n");
            scanf("%d", &size);
            if (size <= 0) {
                printf("Your array can't have negative elements\n");
                size = 0;
                continue;
            }
        }
        break;
    }

    // Then what's the k - in-cluster difference.
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

    // Whether you want to fill the array manually or not.
    int fill = 0;
    printf("How do you want to fill the array?\n1. Random\n2. Manual\n");
    for (;;) {
        scanf("%d", &fill);
        if (fill != 1 && fill != 2) {
            printf("No such option\n");
            continue;
        }
        break;
    }

    arr = calloc(size, sizeof(int));
    srand(time(NULL));

    // Actual array filling in.
    for (int i = 0; i < size; i++) {
        if (fill == 2) {
            printf("\nElement %d:  ", i + 1);
            scanf("%d", &arr[i]);
        } else if (fill == 1) {
            arr[i] = rand() % area;
        }
    }

    // Returning values
    *klu = k;
    *n = size;
    return arr;
}

int comp(const void * elem1, const void * elem2){
    // Function to compare numbers for sorting

    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

static int* calculate(int* source, int const size, int const k){
    // Actual calculations. It's assigns
    // cluster numbers to the right elements

    // init
    int *sorted, *clusters = NULL;
    sorted = calloc(size, sizeof(int));
    clusters = calloc(size, sizeof(int));

    int clust = 1;
    for (int i = 0; i < size; i++){
        clusters[i] = 0;
        sorted[i] = source[i];
    }
    qsort(sorted, size, sizeof(int), comp);

    // Actual comparing with k and assigning.
    int fst = sorted[0];
    for (int i = 0; i < size; i++){
        if (sorted[0] == source[i]){
            clusters[i] = 1;
        }
    }

    for (int i = 1; i < size; i++){
        if (sorted[i] == fst) continue;
        else if (sorted[i] - fst < k){
            ;
        }
        else if (sorted[i] - fst >= k){
            clust += 1;
            fst = sorted[i];
        }
        for (int n = 0; n < size; n++) {
            if (sorted[i] == source[n]) {
                clusters[n] = clust;
            }
        }
    }

    // Freeing and returning
    free(sorted);
    return clusters;
}

int len(int n){
    // Returns the length of a number

    int l = 0, check = 0;
    do{
        n = n / 10;
        if (n == 0) check = 1;
        l++;
    } while (check == 0);
    return l;
}

void spaces(int am){
    // "Important" function to print spaces

    if (am > 1)
    for (int i = 0; i < am; i++) printf(" ");
}

int main() {
    // THE CORE

    // Init
    printf("Hello, World!\n");
    int choice;
    int *src = NULL, *result = NULL;
    int n = 0, k = 0;

    // User interface
    for (;;) {
        printf("\nWhatcha want?\n1. Enter array\n2. "
               "Proceed array\n3. Output array\n4. Exit\n");
        scanf("%d", &choice);

        switch (choice) {
            // Sends to input
            case 1:
                src = input(&n, &k);
                free(result);
                result = NULL;
                break;

            // Proceeds with calculation
            case 2:
                result = calculate(src, n, k);
                break;

            // Prints the result
            case 3:

                printf("[");
                for (int loop = 0; loop < n; loop++) {
                    printf("%-3d ", src[loop]);
                }
                printf("] - source\n");

                printf("[");
                if (result == NULL) {
                    printf("Not proceeded yet");
                } else {
                    for (int loop = 0; loop < n; loop++) {
                        printf("%-3d ", result[loop]);
                        spaces(len(src[loop]) - len(result[loop]));
                    }
                }
                printf("] - clusters\n");
                break;

            // Says goodbye
            case 4: return 0;

            // In case of incorrect option
            default:
                printf("There is no such option :c");
                break;
        }
    }
}
