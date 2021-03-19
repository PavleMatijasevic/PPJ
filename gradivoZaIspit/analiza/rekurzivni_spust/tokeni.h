#ifndef TOKENI
#define TOKENI

#include<stdio.h>
#include<stdlib.h>

#define check_error(userMsg)\
    do{\
        fprintf(stderr, "Sintaksna greska: %s\n", userMsg);\
        exit(EXIT_FAILURE);\
    }while(0)
    
#define EOI  (0)
#define BROJ (1)
#define OZ   (2)
#define ZZ   (3)
#define PLUS (4)
#define PUTA (5)



#endif
