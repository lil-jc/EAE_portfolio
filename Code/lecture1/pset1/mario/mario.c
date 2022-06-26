#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;

    //get user input
    do
    {
        h = get_int("Height: ");
    }
    while (h > 8 || h < 1);

    //loop for height
    for (int i = 0; i < h; i++)
    {
        //loop for left alignment
        for (int k = h - 1; k > i; k--)
        {
            printf(" ");
        }
        //loop for number of # per row
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        //move to next row after completing the row
        printf("\n");
    }


}