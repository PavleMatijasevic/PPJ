%option noyywrap

%{
#include<iostream>
#include<string>
#include<cstdlib>
#include<cstdio>

using namespace std;

#include "broj.hpp"
#include "parser.tab.hpp"

%}


%%

int     {return INT_T;}
print   {return PRINT_T;}
list    {return LIST_T;}

_[a-zA-Z][a-zA-Z0-9]*   {   yylval.ime = new string(yytext);
                            return ID;
                        }
"<<"    { return SHL_T;}
">>"    { return SHR_T;} 
"=="    { return EQ_T;}
"!="    { return NEQ_T;}

"+"     {return PLUS_T;}
"-"		{return MINUS_T;}

[=*/|^~&()\[\]%,\n]	{return *yytext;}

0x[0-9a-fA-F]+	{
					yylval.v = strtol(yytext, NULL, 16);
					return BROJ;
				}
[1-9][0-9]*		{
					yylval.v = strtol(yytext, NULL, 10);
					return BROJ;
				}
0[0-7]*			{
					yylval.v = strtol(yytext, NULL, 8);
					return BROJ;
				}
[ \t]			{ }
.				{
					cerr<<"Leksicka greska: "<<yytext<<endl;
					exit(EXIT_FAILURE);
				}






%%

