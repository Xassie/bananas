#include <stdio.h>
#include <windows.h>

void nod()
{
    int numberOne, numberTwo;   // Actual numbers
    int tempNum;
    char checker = '\0';    // Helper for input

    // First number input
    printf("\nВведите первое число:\n");
    while (scanf("%d%c", &numberOne, &checker, 1) != 2 || checker != '\n' || numberOne <= 0)
    {
        printf("\nВведите положительное число.\n");
        while (getchar() != '\n');
    }

    // Second number input
    printf("\nВведите второе число:\n");
    checker = '\0';
    while (scanf("%d%c", &tempNum, &checker, 1) != 2 || checker != '\n' || tempNum <= 0)
    {
        printf("\nВведите положительное число.\n");
        while (getchar() != '\n');
    }

    // Checking if numbers are the same
    if (numberOne == tempNum)
    {
        printf("\nНаибольший общий делитель равен %d\n", tempNum);
        return;
    }

    // Otherwise checking which one is greater and assigning numbers
    else if (numberOne > tempNum)
    {
        numberTwo = tempNum;
    }
    else
    {
        numberTwo = numberOne;
        numberOne = tempNum;
    }

    int diff = -1;  // Creating difference number
    int result = numberTwo; // Creating number for "end result"
    tempNum = numberOne;

    // Actual comparison loop
    while (1)
    {
        diff = tempNum - (result * (tempNum / result));
        if (diff == 0) break;
        tempNum = result;
        result = diff;
    }

    // Result
    printf("\nНаибольший общий делитель чисел %d и %d равен %d\n", numberOne, numberTwo, result);
}


int main()
{
    // Allowing russian output (screw comments)
    SetConsoleOutputCP(CP_UTF8);
    int choice;

    // Menu UI
    while (1) {
        printf("\nВыберите действие:\n1.Посчитать НОД двух чисел.\n2.Завершить программу\n");

        char checker = '\0';
        while (scanf("%d%c", &choice, &checker, 1) != 2 || checker != '\n') {
            printf("\nВведите непосредственно число\n");
            while (getchar() != '\n');
        }

        switch (choice) {
            case 1:
                nod();
                break;

            case 2:
                return 0;

            default:
                printf("\nТакого варианта нет. Попробуйте ещё раз.\n");
                break;
        }
    }
}