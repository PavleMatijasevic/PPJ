%option noyywrap

%{
#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<map>

using namespace std;

#include "parser.tab.hpp"

%}


%%
"print" {return PRINT_T;}
"def"   {return DEF_T;}
"norm"  {return NORM_T;}
[a-z]+  {
        yylval.niska = new string(yytext);
        return ID_T;}
":="       {return EQ_T;}
[+-]?[0-9]+(\.[0-9]*)?  {
        yylval.vrednost = atof(yytext);
        return BROJ_T;}
\"[^"]+\"   {
    yylval.niska = new string(yytext);
    return FORMAT_T;}
[+(/);:,*-]    {return *yytext;}

[ \t\n] {   }
.   {
    cerr << "Leksicka greska: " << yytext << endl;
    exit(EXIT_FAILURE);
}


%%