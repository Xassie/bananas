
typedef struct point2D
{
    char* name;
    float x;
    float y;
} point2D_t;

typedef struct Figure
{
    char* name;
    int pointsNumber;
    point2D_t* p_array;
} Figure_t;
