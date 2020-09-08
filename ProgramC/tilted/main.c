#include <stdio.h>
#include <string.h>

void printNumbers(char *text)
{
    for (int i=0; i < strlen(text); i++)
    {
        if (text[i] >= '0' && text[i] <= '9')
        {
            printf("%c", text[i]);
        }
    }
    return;
}

int main(void)
{
    char *str = "Some 1-97hdsodme s£bygtext Aligth?";
    printNumbers(str);
    return 0;
}

