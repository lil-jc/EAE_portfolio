#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

bool load(const char *dictionary)
{
    // TODO
    //first word for each letter array
    bool first_word[25];
    for (int i = 0; i < 26; i++)
    {
        first_letter[i] = true;
    }
    char *word = malloc(sizeof(LENGTH));

    //loop until the end of dictionary
    for (int i = 0; i < strlen(dictionary); i++)
    {
        //determine a word
        if (isascii(dictionary[i]) != 0)
        {
            //check if character is a (alphabet) or (') or (-)
            if (isalpha(dictionary[i] != 0 || dictionary[i] = 39 || dictionary[i] = 45))
            {
                word[i] = dictionary[i];
            }
            //check if character is a NULL
            if (dictionary[i] == NULL)
            {
                //run word through hash()
                int letter_position = hash(word);

                //if first word of a letter
                if (first_word[letter_position] = true)
                {
                    //put word into a hash table
                    node *n = malloc(sizeof(node));
                    if (n == NULL)
                    {
                        return 1;
                    }
                    n->word = word;
                    n->next = NULL;
                    table[letter_position] = n;
                    //free word && set first_word = 1
                    free(word);
                    first_word = false;
                }

                //if not first word of letter
                if (first_word[letter_position] = false)
                {
                    //put word into a hash table
                    n = malloc(sizeof(node));
                    if (n == NULL)
                    {
                        for (int i; i < 26; i++)
                        {
                            free(table[i]);
                        }
                        return 1;
                    }
                    n->word = word;
                    n->next = NULL;
                    table[letter_position]->next = n;
                    //free word
                    free(word);
                }

            }
        }