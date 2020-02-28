#include <stdio.h>
#include <malloc.h>

void input(int* n, int** dummy)
{
    int* arr;
    int size = 0;

    for (;;)
    {
        if (size == 0)
        {
            printf("How many elements will array be?\n");
            scanf("%d", &size);
            printf("%i", size);
            if (size <= 0)
            {
                printf("Your array can't have negative elements\n");
                size = 0;
                continue;
            }
        }
        break;
    }

    arr = calloc(size, sizeof(int));
    *n = size;

    for (int i = 0; i < size; i++)
    {
        printf("\nElement %d:  ", i+1);
        scanf("%d", &arr[i]);
        printf("%d ", arr[i]);
    }
    *dummy = arr;
}

static void calculate(int* arr, int* res, ){
    ;
}

int main() {
    printf("Hello, World!\n");
    int c;
    int *src = NULL;
    int n=0;
    n = 0;
    for (;;)
    {
        printf("Whatcha want?\n1. Enter array\n2. Proceed array\n3. Output array\n4. Exit\n");
        scanf("%d", &c);

        if (c == 1)
        {
            input(&n, &src);
        }
        else if(c == 2)
        {
            ;
        }
        else if(c == 3)
        {
            printf("[");
            for (int loop = 0; loop < n; loop++)
            {
                printf("%d ", src[loop]);
            }
            printf("]");
        }
        else if(c == 4)
        {
            break;
        }
    }
    return 0;
}
