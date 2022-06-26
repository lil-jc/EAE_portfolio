#include <math.h>
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float f = get_float("number: ");
    int r = round(f);
    printf("round: %i\n", r);
}