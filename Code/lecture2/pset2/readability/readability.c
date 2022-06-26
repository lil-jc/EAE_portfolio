#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int count_letters(string text_letter);
int count_words(string text_word);
int count_sentences(string text_sentence);

int main(void)
{
    string text = get_string("Text: ");

    //count numbers of letters, words, sentence
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);

    //calculate L & S
    float L = (letters / words) * 100;
    float S = (sentences / words) * 100;

    //calculate grade
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int X = round(index);

    //print grade
    if (X < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (X > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", X);
    }

}
//funtion for counting letters
int count_letters(string TEXT)
{
    int letters = 0;

    //check for every letter if is letter
    for (int i = 0, len = strlen(TEXT); i < len; i++)
    {
        if (isalpha(TEXT[i]))
        {
            letters++;
        }
        else
        {
            letters += 0;
        }
    }

    return letters;
}

//funtion for counting words
int count_words(string TEXT)
{
    int words = 1;

    //check for spaces; for 1 space 1 words
    for (int i = 0, len = strlen(TEXT); i < len; i++)
    {
        if (isspace(TEXT[i]))
        {
            words++;
        }
        else
        {
            words += 0;
        }
    }
    return words;
}

//funtion for counting sentence
int count_sentences(string TEXT)
{
    int sentences = 0;

    //check for '.' or '!' or '?'; if yes at 1 to sentence
    for (int i = 0, len = strlen(TEXT); i < len; i++)
    {
        if (TEXT[i] == '.')
        {
            sentences++;
        }
        else if (TEXT[i] == '!')
        {
            sentences++;
        }
        else if (TEXT[i] == '?')
        {
            sentences++;
        }
        else
        {
            sentences += 0;
        }
    }
    return sentences;
}