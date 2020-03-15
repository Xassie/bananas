#include <stdio.h>
#include <malloc.h>
#include <time.h>

int** input(int* vsize, int* hsize)
{
    int n = 0;
    int m = 0;
    char check = '\0';
    int const range = 40;

    printf("\nHow many lines should matrix have?\n");
    while (scanf("%d%c", &n, &check, 1) != 2  || check != '\n' || n <= 0)
    {
        printf("Please enter valid and positive number");
        while (getchar() != '\n')
            ;
    }

    check = '\0';
    printf("\nHow many rows should matrix have?\n");
    while (scanf("%d%c", &m, &check, 1) != 2  || check != '\n' || n <= 0)
    {
        printf("Please enter valid and positive number");
        while (getchar() != '\n')
            ;
    }

    int fill = 0;
    check = '\0';
    printf("\nHow do you want to fill the array?\n1. Random\n2. Manual\n");
    while ((scanf("%d%c", &fill, &check, 1) != 2  || check != '\n') || (fill != 1 && fill != 2))
    {
        printf("No such option\n");
        while (getchar() != '\n')
            ;
    }
    srand(time(NULL));

    int** arr = (int **)malloc(sizeof(int*) * n);
    for (int i=0; i < n; i++)
        arr[i] = (int*)malloc(sizeof(int) * m);
    int num = 0;

    for (int i=0; i<n; i++)
    for (int j=0; j<m; j++)
    {
        if (fill == 2)
        {
            num = 0;
            check = '\0';
            printf("(%d;%d) = ", i, j);
            while (scanf("%d%c", &num, &check, 1) != 2 || check != '\n') {
                printf("\nPlease enter valid number\n");
                while (getchar() != '\n');
            }
            arr[i][j] = num;
        }
        else if (fill == 1)
            arr[i][j] = rand() % range;
    };

    *vsize = n;
    *hsize = m;
    return arr;
}

void arrfree(int ***arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        int** dummy = (int **)arr[i];
        free(dummy);
    }
    free(*arr);
}


int main() {
    int vsize=0, hsize=0;
    int** source = NULL;
    int choice;

    while (1)
    {
        printf("\nWhatcha want?\n1. Enter new info\n2. "
               "Rotate matrix\n3. Output matrix\n4. Exit\n");
        char checker = '\0';
        while (scanf("%d%c", &choice, &checker, 1) != 2 || checker != '\n') {
            printf("\nPlease enter valid number\n");
            while (getchar() != '\n');
        }

        switch (choice)
        {

            case 1:
                if (source != NULL)
                    for (int i=0; i<vsize; i++)
                    {
                        int* dummy = source[i];
                        free(dummy);
                    }
                    free(source);
                source = input(&vsize, &hsize);
                break;

            case 2:
                if (source != NULL)
                {
                    int number = 0;
                    char check = '\0';

                    printf("\nRotate by how many degrees counterclock-wise?\n");
                    while (scanf("%d%c", &number, &check, 1) != 2 || check != '\n' || number % 90 != 0) {
                        printf("\nPlease enter a number multiple of 90\n");
                        while (getchar() != '\n');
                    }

                    switch ((number % 360)) {
                        case 0:
                            break;

                        case 90: {
                            int **mirror = (int **) malloc(sizeof(int *) * vsize);
                            for (int i = 0; i < vsize; i++) {
                                mirror[i] = (int *) malloc(sizeof(int) * hsize);
                                for (int j = 0; j < hsize; j++)
                                    mirror[i][j] = source[i][j];
                            }

                            arrfree(&source, vsize);
                            source = (int **) malloc(sizeof(int *) * hsize);
                            for (int i = 0; i < hsize; i++)
                                source[i] = (int *) malloc(sizeof(int) * vsize);

                            for (int i = 0; i < hsize; i++)
                                for (int j = 0; j < vsize; j++)
                                    source[i][j] = mirror[j][hsize - 1 - i];

                            arrfree(&mirror, vsize);
                            int k = hsize;
                            hsize = vsize;
                            vsize = k;
                            break;
                        }

                        case 180: {
                            int **mirror = (int **) malloc(sizeof(int *) * vsize);
                            for (int i = 0; i < vsize; i++) {
                                mirror[i] = (int *) malloc(sizeof(int) * hsize);
                                for (int j = 0; j < hsize; j++)
                                    mirror[i][j] = (int) source[i][j];
                            }

                            for (int i = 0; i < vsize; i++)
                                for (int j = 0; j < hsize; j++) {
                                    source[i][j] = (int) mirror[vsize - 1 - i][hsize - 1 - j];
                                }
                            arrfree(&mirror, vsize);
                            break;
                        }

                        case 270: {
                            int **mirror = (int **) malloc(sizeof(int *) * vsize);
                            for (int i = 0; i < vsize; i++) {
                                mirror[i] = (int *) malloc(sizeof(int) * hsize);
                                for (int j = 0; j < hsize; j++)
                                    mirror[i][j] = source[i][j];
                            }

                            arrfree(&source, vsize);
                            source = (int **) malloc(sizeof(int *) * hsize);
                            for (int i = 0; i < hsize; i++)
                                source[i] = (int *) malloc(sizeof(int) * vsize);

                            for (int i = 0; i < hsize; i++)
                                for (int j = 0; j < vsize; j++)
                                    source[i][j] = mirror[vsize-1-j][i];

                            arrfree(&mirror, vsize);
                            int k = hsize;
                            hsize = vsize;
                            vsize = k;
                            break;
                        }

                        default:
                            break;
                    }
                    break;
                }


            case 3:
                if (source != NULL)
                {
                    printf("\n");
                    for (int i=0; i<vsize; i++)
                    {
                        for (int j = 0; j < hsize; j++)
                            printf("%-3d ", source[i][j]);
                        printf("\n");
                    }
                }
                else
                    printf("\nIt is not yet proceeded\n");
                break;

            case 4:
                return 0;

            default:
                printf("There is no such option :c");
                break;
        }
    }
}
