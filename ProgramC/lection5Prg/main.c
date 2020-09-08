#include <stdio.h>
#include <stdlib.h>
#include "structure.h"
#include "functions.h"


int main()
{
    printf("Программа создаёт фигуры по точкам и находит их периметр\n");

    Figure_t figure = {NULL, 0, NULL};  // Создаём фигуру
    printf("\nВведите имя фигуры: ");
    // и устанавливаем её имя
    figure.name = enterStr();

    printf("\nСколько точек в фигуре: ");
    int pointsNumber = 0;
    scanf("%d", &pointsNumber);

    for (int i = 0; i < pointsNumber; ++i)
    {
        point2D_t tmpPoint = {NULL, 0, 0};
        printf("\nВведите имя точки: ");
        getchar();
        tmpPoint.name = enterStr();

        printf("\nВведите координаты точки %s\nx = ", tmpPoint.name);
        scanf("%f", &tmpPoint.x);
        printf("y = ");
        scanf("%f", &tmpPoint.y);

        addPoint2Figure(&figure, tmpPoint);
    }

    printf("\nСозданная фигура:");
    printf("\nИмя: %s", figure.name);
    printf("\nКоличество углов (точек): %d", figure.pointsNumber);
    printf("\nТочки:");
    float perimeter = 0;
    for (int i = 0; i < figure.pointsNumber; ++i)
    {
        printf("\n");
        ShowPoint(&figure.p_array[i]);

        if (i > 0)
            perimeter += PythagoreanTheorem(figure.p_array[i - 1]
                                          , figure.p_array[i]);
    }
    printf("\nПериметр: %f", perimeter);

    // Очищаем память
    for (int i = 0; i < pointsNumber; ++i)
        free(figure.p_array[i].name);

    free(figure.p_array);
    free(figure.name);

    return 0;
}
