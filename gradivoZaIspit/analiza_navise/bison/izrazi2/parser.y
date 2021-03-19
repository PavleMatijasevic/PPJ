%{
#include<stdio.h>
#include<stdlib.h>

extern int yylex();

int yyerror(char* s){
    fprintf(stderr, "Sintaksna greska: %s\n", s);
    exit(EXIT_FAILURE);
    }

%}
%union{
    float v;
}

%token<v> BROJ
%type<v> e

%left '+' '-'
%right '/' '*'
%left UMINUS


%%
pocetak: pocetak naredba
       | naredba
       ;
naredba: e ';'           {printf("Vrednost je %.2f\n",$1);}
       ;
e:   e '+' e             {$$ = $1 + $3;}
    |e '-' e             {$$ = $1 - $3;}   
    |e '*' e             {$$ = $1 * $3;}
    |e '/' e             {$$ = $1 / $3;}
    |'(' e ')'           {$$ = $2;}
    | '-' e %prec UMINUS {$$ = -$2;}   
    | BROJ               {$$ = $1;}
    ;
%%


int main(){
    if(yyparse() == 0){
        printf("Sintaksna analiza je uspesno prosla\n");
    }
    else{
    printf("Sintaksna analiza nije uspela\n");
    }


    exit(EXIT_FAILURE);
    }
