#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //dynamically allocate an array of size 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    //assign three numbers to the array
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    //time passes i need more space

    //resize old array to be of size 4
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }
    tmp[3] = 4;

    //copy from tmp file back to list

    //realloc will free tmp no need to free tmp
    list = tmp;

    //print array
    for(int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    //freeing the list is also freeing tmp because list is pointing at tmp
    free(list);
    return 0;

}