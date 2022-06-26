#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char a = get_char("letter: ");
    int i = sizeof(a);
    printf("sizeof(a) = %i\n", i);
}