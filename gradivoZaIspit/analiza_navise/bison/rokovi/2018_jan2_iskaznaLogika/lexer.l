%option noyywrap

%{
#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstdio>

using namespace std;
#include "parser.tab.hpp"

%}


%%

"True"  {yylval.vrednost = 1;
        return VAL_T;}
"False" {yylval.vrednost = 2;
        return VAL_T;}
"Undef" {yylval.vrednost = 0;
        return VAL_T;}
"head"  {return HEAD_T;}
"tail"  {return TAIL_T;}
[a-z][a-z0-9]*  {
    yylval.ime = new string(yytext);
    return ID_T;
}
[A-Z][A-Z0-9]*  {
    yylval.ime = new string(yytext);
    return IDL_T;
}
":="            {return EQ_T;}
"<=>"           {return EQUI_T;}
"=>"            {return IMPL_T;}
"\\/"           {return OR_T;}
"/\\"           {return AND_T;}
"!"             {return NEQ_T;}
[\n(),\[\]]     {return *yytext;}
[ \t]           {   }
0|[1-9][0-9]*   {yylval.vrednost =  strtol(yytext, NULL, 10);
                return BROJ_T;}
.               {
    cerr << "Leksicka greska: " << yytext << endl;
    exit(EXIT_FAILURE);
}


%%  