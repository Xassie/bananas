#include <math.h>
#include "structure.h"

#define BACKSPACE_KEY 8
#define START_CHAR_RANGE 32
#define END_CHAR_RANGE 126


float PythagoreanTheorem(point2D_t point1, point2D_t point2)
{
    // Считаем расстояние по теореме Пифагора
    return sqrtf(pow(point2.x - point1.x, 2) + pow(point2.y - point1.y, 2));
}

void ShowPoint(point2D_t* point)
{
    printf("(%.3f, %.3f)", point->x, point->y);
}

//Используем функцию для ввода строки из лекции 3
char* enterStr()
{
    char* userStr = (char*)malloc(1 * sizeof(char));
    userStr[0] = '\0';
    char curChar = 0;
    int curSize = 1;

    while(curChar != '\n')
    {
        curChar = getchar();
        int deltaVal = 0; // Определяет, на сколько изменится длина массива
        int lengthDif = 0;
        // Если мы ситраем символы, а не пишем их,
        if (curChar == BACKSPACE_KEY)
        {
            deltaVal = -1; // то будем уменьшать длину массива
            lengthDif = 1; // и копировать строку до предпоследнего символа
        }
        // Иначе проверяем, входит ли введённый символ в диапазон печатных
        else
        {
            if (curChar >= START_CHAR_RANGE && curChar <= END_CHAR_RANGE)
            {
                deltaVal = 1; // Если да, то будем увеличиватьдлину на 1
                lengthDif = 2; // Не заполняем последние 2 символа -
                // оставлем мето для введённого символа и \0
            }
            else
                continue; // Если это не печатный символ, то пропускаем его
        }
        // Если стирать больше нечего, но пользователь всё равно жмёт Backspace,
        int newSize = curSize + deltaVal;
        if (newSize == 0)
            continue; // то мы переходим на следующую итерацию - ждём '\n'

        char* tmpStr = (char*)malloc(newSize * sizeof(char));
        if (tmpStr) // Проверяем, выделилась ли память
        {
            // Идём до предпоследнего символа, т.к. надо в конец записать 0
            for (int i = 0; i < newSize - lengthDif; ++i)
            tmpStr[i] = userStr[i];
            if (curChar != BACKSPACE_KEY) // Если введён печатный символ,
                tmpStr[newSize - 2] = curChar; // Добавляем его в строку
            tmpStr[newSize - 1] = '\0';
            free(userStr);
            userStr = tmpStr;
            curSize = newSize;
        }
        else
        {
            printf("Не могу выделить память под обновлённоу строку!");
            break;
        }
        // Теперь печатаем введённый символ
        printf("%c", curChar);
    }

    return userStr;
}

// Функция добавления точки в фигуру
void addPoint2Figure(Figure_t* figure, point2D_t point)
{
    int newArrSize = figure->pointsNumber + 1;
    point2D_t* tmpArr = (point2D_t*)malloc(newArrSize * sizeof(point2D_t));

    for (int i = 0; i < figure->pointsNumber; ++i)
        tmpArr[i] = figure->p_array[i];

    tmpArr[newArrSize - 1] = point;
    free(figure->p_array);
    figure->p_array = tmpArr;
    figure->pointsNumber = newArrSize;
}
