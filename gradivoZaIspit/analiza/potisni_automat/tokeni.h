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

    
#define E		(100)
#define EP		(101)
#define T		(102)
#define TP		(103)
#define F		(104)

    
#endif
