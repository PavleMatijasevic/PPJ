/* E -> T EP			(, BROJ
 * TP -> + T EP			+
 * 		eps				), EOI
 * T -> F TP			(, BROJ
 * TP -> * F TP			*
 *      eps				+, ZZ, EOI
 * F -> ( E )			(
 * 		BROJ			BROJ
 */

#include<stdio.h>
#include<stdlib.h>

#include "tokeni.h"

extern int yylex();
int preduvid = 0;

void E(void);
void EP(void);
void T(void);
void TP(void);
void F(void);

int main(int argc, char** argv){

    preduvid = yylex();
    E();
    if(preduvid == EOI){
        printf("Sve je okej!\n");
    }
    else{
        printf("Sintaksna greska! Visak tokena na ulazu!\n");
    }
    

    exit(EXIT_SUCCESS);
}


void E(void){
    if(preduvid == OZ || preduvid == BROJ){
        T();
        EP();
    }
    else{
     check_error("Ocekivao sam OZ ili BROJ!\n");
    }
}
void EP(void){
    if(preduvid == PLUS){
        preduvid = yylex();
        T();
        EP();
    }
    else if(preduvid == EOI || preduvid == ZZ){
        return;
    }
    else{
        check_error("Ocekivao sam PLUS ili EOI ili ZZ\n");
    }
}
void T(void){
    if(preduvid == OZ || preduvid == BROJ){
        F();
        TP();
    }
    else{
        check_error("Ocekivao sam OZ ili BROJ!\n");
    }
}
void TP(void){
    if(preduvid == PUTA){
        preduvid = yylex();
        F();
        TP();
    }
    else if(preduvid == PLUS || preduvid == EOI || preduvid == ZZ){
        return;
    }
    else{
        check_error("Ocekivao sam PUTA ili PLUS ili EOI ili ZZ\n");
    }
    
}
void F(void){
    if(preduvid == OZ){
        preduvid = yylex();
        E();
        if(preduvid != ZZ)
            check_error("Ocekivao sam ZZ\n");
        preduvid = yylex();
    }
    else if(preduvid == BROJ){
        preduvid = yylex();
        
    }
    else{
    
        check_error("Ocekivao sam OZ ili ZZ\n");
    }
}






















