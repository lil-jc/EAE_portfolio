# include <stdio.h>
# include <cs50.h>

int main(void)
{
    //make variables
    string(name);
    string(age);
    string(happy);

    //asign strings with value
    name = get_string("what's your name?: ");
    age = get_string("how old are you?: ");
    happy = ("how are you doing?");

    //print output
    printf("hello, %s. you are %s years old. %s\n", name, age, happy);
}