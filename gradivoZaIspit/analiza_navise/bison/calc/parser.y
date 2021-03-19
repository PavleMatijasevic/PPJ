%{

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

extern int yylex()

int yyerror(char* s){
    fprintf(stderr, "Greska u sintaksi: %s\n",yytext);
    exit(EXIT_FAILURE);
}





%}

%union{
    float v;
    char* ime;
}


%left '+' '-'
%right '/' '*'
%left UMINUS

%token<v> BROJ
%token<ime> ID
%token PRINT LEQ GEQ NEQ EQ

%type<v> e

%start program

%%

program: program naredbe ';'
        | naredbe ';'
        ;
naredbe: PRINT '(' e ')'
       | ID '=' e
       | e '>' e
       | e '<' e
       | e 'GEQ' e
       | e 'LEQ' e
       | e 'NEQ' e
       | e 'EQ'  e
       ;
e: e '+' e
|  e '-' e
|  e '*' e
|  e '/' e
|  '-' e %prec UMINUS
| BROJ
| '(' e ')'
| ID
;


%%

int main(){
    alociraj();

    if(yyparse() == 0){
        printf("Sve je ok proslo\n");
        }
    else{
    printf("Nije uspela sintaksna analiza\n");
    }   


    exit(EXIT_SUCCESS);
    }
