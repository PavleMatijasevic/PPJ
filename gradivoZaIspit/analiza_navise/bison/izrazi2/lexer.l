%option noyywrap

%{

#include "parser.tab.h"

%}

%%

[0-9]+(\.[0-9]*)?   {   yylval.v = atoi(yytext);
                        return BROJ;
                    }
[+*/\-;()]            {return *yytext;}
[ \t\n]             { }
.                   {
                    printf("Leksicka analiza neuspesna: %s\n", yytext);
                    exit(EXIT_FAILURE); 
                    }


%%
