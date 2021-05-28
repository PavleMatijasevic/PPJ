%option noyywrap

%{
#include<iostream>

#include "parser.tab.hpp"

using namespace std;
%}

%%

"rofl"      {return PRINT_T;}
"ktnxbye"   {return BYE_T;}
"orly?"     {return COND_T;}
"iz"        {return IZ_T;}
"uber"      {return GT_T;}
"liek"      {return EQ_T;}
"nope"      {return NEQ_T;}

lo{1,48}l {   
    for(int i = 0; yytext[i] != '\0'; i++)
    yytext[i] = toupper(yytext[i]);
    yylval.ime = new string(yytext);
    return ID_T;
}
[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]    {
    yylval.vrednost = strtol(yytext, NULL, 10);
    return BROJ_T;
}
"++"    {return INC_T;}
"--"    {return DEC_T;}

[\n+()*-]   {return *yytext;}
[ \t]   { }
. {
    cout << "Leksicka greska!" << endl;
    exit(EXIT_FAILURE);
}   

%%