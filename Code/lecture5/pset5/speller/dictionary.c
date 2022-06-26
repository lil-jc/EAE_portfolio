// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 25;
// Hash table
node *table[N];
int total_words = 0;





// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //pass through hash() to get index
    int index = hash(word);
    //make a tmp table & run through the table
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}





// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int index;
    //find the ASCII number of first letter of word
    for (int i = 0; i < 26; i++)
    {
        if (toupper(word[0]) == 'A' + i)
        {
            index = i;
        }
    }
    //return the ASCII number corresponding to the first letter of word
    return index;
}





// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file != NULL)
    {
        char word[LENGTH + 1];
        //read from file till the end
        while (fscanf(file, "%s", word) != EOF)
        {
            //create a new tmporary node and store word in it
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return false;
            }
            strcpy(n->word, word);
            n->next = NULL;
            //pass word into hash() to get letter_position
            int index = hash(word);
            //append n into table
            if (table[index] != NULL)
            {
                table[index] = n;
            }
            else
            {
                n->next = table[index];
                table[index] = n;
            }
            total_words++;
        }
        fclose(file);
        return true;
    }
    else
    {
        fclose(file);
        return false;
    }
}





// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total_words;
}





// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //for every bucket of table
    for (int i = 0; i < 26; i++)
    {
        node *tmp = table [i];
        node *cursor = table [i];
        while (tmp != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
