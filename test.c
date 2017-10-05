#include <stdio.h>
#include <string.h>

int foo(void)
{
    puts("From the shared library!");
    return 0;
}

int take_char_array(char c[])
{
    if (!strcmp(c, "Testing!")) {
        return 1;
    }
    printf("string == '%s'\n", c);
    return 0;
}

int ivi_dance(int s, char c[])
{
    if (s == 0) {
        return strlen("42 is the answer to the ultimate question.");
    }
    strcpy(c, "42 is the answer to the ultimate question.");
    return 0;
}


int fixed(int s, char c[])
{
    strncpy(c, "43 is better!", s);
    return 0;
}
