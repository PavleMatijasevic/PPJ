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
"niska"     {return NISKA_T;}
"obrni"     {return OBRNI_T;}
"sortiraj"  {return SORTIRAJ_T;}
"duzina"    {return DUZINA_T;}
"podniska"  {return PODNISKA_T;}
"velika"    {return VELIKA_T;}
"mala"      {return MALA_T;}
"stampaj"   {return STAMPAJ_T;}
"=="        {return EQ_T;}
">"         {return GT_T;}
"<"         {return LT_T;}
"+="        {return INC_T;}

\"[^\"]+\"  {
    yylval.ime = new string(yytext);
    return CONST_T;
}
0|[1-9]|[1-9][0-9]* {
    yylval.vrednost = strtol(yytext, NULL, 10);
    return BROJ_T;
}
[a-z][a-z0-9_]*  {
    yylval.ime = new string(yytext);
    return ID_T;
}
["=\[\]();.+-]
[ \t\n] {   }
.   {
    cerr << "Leksicka greska: " << yytext << endl;
    exit(EXIT_FAILURE);
}

%%