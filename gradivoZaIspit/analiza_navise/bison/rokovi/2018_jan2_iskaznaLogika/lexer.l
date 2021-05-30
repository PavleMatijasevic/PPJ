%option noyywrap

%{
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<map>
#include<vector>
using namespace std;

#include "parser.tab.hpp"

%}

%%

"True"          {
    yylval.vrednost = 1;
    return VAL_T;}
"False"         {
    yylval.vrednost = 2;
    return VAL_T;}
"Undef"         {
    yylval.vrednost = 0;
    return VAL_T;}
"head"          {return HEAD_T;}
"tail"          {return TAIL_T;}
":="            {return EQ_T;}
[a-z][a-z0-9]*  {
    yylval.ime = new string(yytext);
    return ID_T;
}
"/\\"        {return AND_T;}
"\\/"        {return OR_T;}
"=>"        {return IMPL_T;}
"<=>"       {return EQUI_T;}
"!"         {return NEQ_T;}
0|[0-9]+    {
    yylval.vrednost = strtol(yytext, NULL, 10);
    return BROJ_T;
}
[A-Z][A-Z0-9]* {
    yylval.ime = new string(yytext);
    return IDL_T;}
[\n()\[\],] {return *yytext;}
[ \t]   {   }
.   {
    cerr << "Leksicka greska: " << yytext << endl;
    exit(EXIT_FAILURE);
}



%%