#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//prototype
string cipher(string word, int move);

int main(int argc, string argv[])
{
    int arg = atoi(argv[1]);
//acept only 2 as argc
    if (argc != 2 || argc == 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (argc == 2)
    {
        string s = get_string("plaintext: ");

        string caesar = cipher(s, arg);
        printf("ciphertext: %s\n", caesar);
        return 0;
    }

}
//funtion to cypher the str
string cipher(string word, int move)
{
    char new_cypher[strlen(word)];

    for (int i = 0, len = strlen(word); i < len; i++)
    {
        //cypher for uppercase
        if (isupper(word[i]))
        {
            int p = (int)word[i] - 'A';
            int c = (p + move) % 26;
            char cypher = c + 'A';
            new_cypher[i] = cypher;
        }
        //cypher for lowercase
        else if (islower(word[i]))
        {
            int p = (int)word[i] - 'a';
            int c = (p + move) % 26;
            char cypher = c + 'a';
            new_cypher[i] = cypher;
        }
        //not cyfering the non-aphabets
        else
        {
            char cypher = word[i];
            new_cypher[i] = cypher;
        }
    }
    //remember to return
    string new_string = (string)new_cypher;
    return new_string;
}
