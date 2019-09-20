#include <iostream>
#include <conio.h>
#include <windows.h>
using namespace std;
int main()

{
SetConsoleCP(1251);
SetConsoleOutputCP(1251);
char fio[256];
double summa;
double nalog;
double trans;
double chek;
cout « "Введите ФИО покупателя ";
cin.getline(fio, 256);
cout « "Введите сумму заказа ";
cin » summa;
nalog = summa * 0.06;
trans = summa * 0.1;
chek = summa + nalog + trans;
cout « "\t\t\t НАКЛАДНАЯ\n"
« " ____________________________________________________"
« "\n ПОКУПАТЕЛЬ \t\t" « fio
« "\n Сумма заказа \t\t" « summa
« "\n Налог \t\t\t" « nalog
« "\n Транспортировка \t" « trans
« "\n ____________________________________________________"
« "\n Стоимость всего \t" « chek
« "\n ____________________________________________________"«"\n";
system("pause");
}