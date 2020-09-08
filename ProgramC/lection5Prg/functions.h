#ifndef FUNCTIONS_H_INCLUDED
#define FUNCTIONS_H_INCLUDED

float PythagoreanTheorem(point2D_t, point2D_t);
void ShowPoint(point2D_t*);
// Используем функцию для ввода строки из лекции 3
char* enterStr(void);
// Функция добавления точки в фигуру
void addPoint2Figure(Figure_t*, point2D_t);

#endif // FUNCTIONS_H_INCLUDED
