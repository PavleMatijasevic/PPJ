#ifndef TOKENI
#define TOKENI

#include<stdlib.h>
#include<stdio.h>


#define check_error(cond, usrMes)\
    do{\
        if(!cond){\
            fprintf(stderr, "Sintaksna greska: %s\n", usrMes);\
            exit(EXIT_FAILURE);\
        }\
    }while(0)


#define EOI     (0)
#define BROJ    (1)
#define OZ      (2)
#define ZZ      (3)
#define PLUS    (4)
#define PUTA    (5)


