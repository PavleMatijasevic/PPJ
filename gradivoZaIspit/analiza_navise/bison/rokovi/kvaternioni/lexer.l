%option noyywrap

%{

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

#include "kvaternioni.hpp"
#include "parser.tab.hpp"

%}

%%

def		{ return DEF_T;}
print 	{ return PRINT_T;}
norm 	{ return NORM_T;}
["][^"]+["]	{
					yylval.ime = new string(yytext);
					return FMT_STRING;
			}
-?[0-9]+(\.[0-9]*)?	{
						yylval.v = atof(yytext);
						return BROJ;
					}
[a-zA-Z][a-zA-Z0-9_]* {
						yylval.ime = new string(yytext);
						return ID;
					}
":=" 	{return DODELA;}
[():;,+*/%-]	{return *yytext; }
[ \t\n]	{ }
.		{
			cerr<<"Leksicka greska: "<<yytext<<endl;
			exit(EXIT_FAILURE);
		}

%%

