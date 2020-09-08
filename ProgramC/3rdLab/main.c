#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define BACKSPACE 8
#define START_RANGE 32
#define END_RANGE 123
#define START_UPPER 65
#define END_UPPER 91
#define START_LOWER 97
#define END_LOWER 123
#define MIDDLE_CHAR 110
#define LINE_END 10
#define READ_PATH "..\\text.txt"
#define WRITE_PATH "..\\result.txt"

char* input(int* csize)
// Manual string input
{
    // Allocating memory to the string of \0
    char* userString = (char*)malloc(1 * sizeof(char));
    userString[0] = '\0';
    char nextChar = 0;
    int currentSize = 1;
    bool spaced = false;
    printf("Type in the text: \n");

    while(nextChar != '\n')
    {
        // Getting next character of the input
        nextChar = (char)getchar();
        // delta to detect how string will change
        int delta = 0;
        int lengthDif = 0;

        if (nextChar == BACKSPACE)
        // in case of backspace event we need to clear one char => delta = -1
        {
            delta = -1;
            lengthDif=1;
        }

        else if (nextChar == LINE_END)
        // Catching end line char and force-continuing (ending)
        {
            continue;
        }

        else
        {
            if (nextChar >= START_RANGE && nextChar <= END_RANGE)
            // checking if char is in needed range
            {
                if (nextChar == START_RANGE)
                // START_RANGE == 32 and represents space char
                {
                    if (spaced)
                    // if we have space on previous char, we skip it
                    {
                        continue;
                    }
                    delta = 1;
                    lengthDif = 2;
                    spaced = true;
                }
                else if (nextChar >= START_LOWER && nextChar < END_LOWER)
                {
                    // proceeding lowercase letters
                    delta = 1;
                    lengthDif = 2;
                    spaced = false;
                }

                else if (nextChar >= START_UPPER && nextChar < END_UPPER)
                {
                    // in case of uppercase letter we change character to its lower case version
                    nextChar += 32;
                    delta = 1;
                    lengthDif = 2;
                    spaced = false;
                }

                else
                    continue;
            }
        }

        // "Calculating" new size of the string
        int newSize = currentSize + delta;
        if (newSize == 0)
        // catching possible backspace event
        {
            continue;
        }
        // creating temporary string
        char* tempStr = (char*)malloc(newSize * sizeof(char));

        if (tempStr)
        // if memory successfully allocated then..
        {
            for (int i = 0; i < newSize - lengthDif; ++i)
            // filling temp string with previous symbols
            {
                tempStr[i] = userString[i];
            }

            if (nextChar != BACKSPACE)
            // adding new char to the string if it wasn't backspace
            {
                tempStr[newSize - 2] = nextChar;
            }

            // Actually making it a string
            tempStr[newSize - 1] = '\0';
            // Freeing previous string
            free(userString);
            // and assigning temp to user string
            userString = tempStr;
            // updating size
            currentSize = newSize;
        }

        else
        {
            printf("Unable to allocate memory");
            break;
        }
    }
    // Returning values
    *csize = currentSize;
    return userString;
}

void encode(char* src, int const ssize)
{
    // If source string is not empty
    if (src)
    {
        // Then we change every char apart from space
        int size = ssize;
        char nextChar = 0;
        for (int i = 0; i < size-1; i++)
        {
            nextChar = src[i];

            if (nextChar != 32 && nextChar < MIDDLE_CHAR)
            // If character is before middle element of alphabet then we add
            {
                nextChar += 13;
            }
            else if (nextChar != 32 && nextChar >= MIDDLE_CHAR)
            // And the opposite
            {
                nextChar -= 13;
            }
            // Replacing character
            src[i] = nextChar;
        }
    }
}

char* fileRead(int* csize) {
    // Basically the same as for user input
    char *userString = (char *) malloc(1 * sizeof(char));
    userString[0] = '\0';
    int currentSize = 1;
    bool spaced = false;

    int c;
    // Creating a pointer and opening the file with Read mode
    FILE *file;
    file = fopen(READ_PATH, "r");
    if (file) {
        // While not the end of the file - check
        while ((c = getc(file)) != EOF) {
            // Everything below is almost as input func
            int delta = 0;
            int lengthDif = 0;
            if (c >= START_RANGE && c <= END_RANGE) {
                if (c == START_RANGE)
                {
                    if (spaced)
                    {
                        continue;
                    }
                    delta = 1;
                    lengthDif = 2;
                    spaced = true;

                }
                else if (c >= START_LOWER && c < END_LOWER)
                {
                    delta = 1;
                    lengthDif = 2;
                    spaced = false;
                }
                else if (c >= START_UPPER && c < END_UPPER)
                {
                    c += 32;
                    delta = 1;
                    lengthDif = 2;
                    spaced = false;
                }
                else
                    continue;
            }

            int newSize = currentSize + delta;
            if (newSize == 0) {
                continue;
            }

            char *tempStr = (char *) malloc(newSize * sizeof(char));

            if (tempStr) {
                for (int i = 0; i < newSize - lengthDif; ++i) {
                    tempStr[i] = userString[i];
                }

                tempStr[newSize - 2] = (char)c;
                tempStr[newSize - 1] = '\0';
                free(userString);
                userString = tempStr;
                currentSize = newSize;
            }
        }
        *csize = currentSize;
        // Closing the file
        fclose(file);
        return userString;
    }
    else
    {
        printf("\nError. Unable to open the file.\n");
    }
}

void fileWrite(char* src, int const ssize)
{
    // Opening the file in Write mode
    FILE* file;
    file = fopen(WRITE_PATH, "w");
    if (file)
    {
        // Printing every character in it.
        for (int i = 0; i < ssize-1; i++)
        {
            fprintf(file, "%c", src[i]);
        }
        fclose(file);
    }
}

int main()
{
    char* string = NULL;
    int size = 0;
    int choice;

    while (1)
    {
        printf("What do you want to do?\n1.Input new string\n2.Proceed string\n3.Display string\n"
               "4.Read text from the file\n5.Write text into the file\n6.Exit\n");

        char checker = '\0';
        while (scanf("%d%c", &choice, &checker, 1) != 2 || checker != '\n') {
            printf("\nPlease enter a valid number\n");
            while (getchar() != '\n');
        }

        switch (choice)
        {
            case 1:
                if (string)
                {
                    free(string);
                }
                string = input(&size);
                break;

            case 2:
                if (string)
                {
                    encode(string, size);
                }
                else
                {
                    printf("\nThere is no string yet\n");
                }
                break;

            case 3:
            {
                if (string) {
                    printf("\n>>> %s\n", string);
                }
                else
                {
                    printf("\nError. There is no string yet.\n");
                }
                break;
            }

            case 4:
                if (string)
                {
                    free(string);
                }
                string = fileRead(&size);
                break;

            case 5:
                if (string)
                {
                    fileWrite(string, size);
                }
                else
                {
                    printf("\nThere is nothing to write yet.\n");
                }
                break;

            case 6:
                free(string);
                return 0;

            default:
                printf("\nThere is no such option\n");
                break;
        }
    }
}
