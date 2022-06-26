#include <stdio.h>
#include <stdlib.h>

//type def defined the word node
//struct define the type if data that node is
typedef struct node
{
    int number;
    struct node *next;
}
node;
//number is where you store a int
//next is just a pointer of you need to point to another list

int main(void)
{
    //list of numbers
    node *list = NULL;

    //add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;

    //update list to be the same as n
    list = n;

    //add another number
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    //point pointer of list to n
    list->next = n;

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    //point pointyer of list to n
    list->next->next = n;

    //print numbers
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }

    //free link list
    while (list !=NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return 0;

}