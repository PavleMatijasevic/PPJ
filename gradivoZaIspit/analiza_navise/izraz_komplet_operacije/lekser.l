%option noyywrap

%{
    #include "tokeni.h"
    extern int yylval;
%}

%%
[0-9]+  {yylval = atoi(yytext);
        return BROJ;}
"+"     {return PLUS;}
"*"     {return PUTA;}
"/"     {return PODELJENO;}
"-"     {return MINUS;}
")"     {return ZZ;}
"("     {return OZ;}
[ \t\n] {   }
.       {
        fprintf(stderr, "Leksicka greska: %s\n" , yytext);
        exit(EXIT_FAILURE);
        }
%%
