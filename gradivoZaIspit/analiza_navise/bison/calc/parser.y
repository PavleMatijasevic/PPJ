%{

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INIT_CAP (32)
#define STEP	(2)

extern int yylex();

int yyerror(char* s) {
	
	fprintf(stderr, "Sintaksna greska: %s\n", s);
	exit(EXIT_FAILURE);
}


typedef struct {

	char* ime;
	float v;
} prom_t;

prom_t* promenljive = NULL;
int capacity;
int n;

void alociraj(){
	
	capacity = INIT_CAP;
	n = 0;
	
	promenljive = malloc(capacity*sizeof(prom_t));
	
	if (promenljive == NULL) {
	
		fprintf(stderr, "init");
		exit(EXIT_FAILURE);
	}
}

void dealociraj(){

	int i = 0;
	
	for (i = 0; i < n; i++) {
		
		free(promenljive[i].ime);
	}
	
	free(promenljive);
}

int pronadji(char* s){

	int i = 0;

	for (i = 0; i < n; i++) {
	
		if (strcmp(promenljive[i].ime, s) == 0) {
			return i;
		}
	}
	
	return -1;
}

%}

%union{

	float v;
	char* ime;
}

%left '+' '-'
%left '*' '/'
%right UMINUS

%token<v> BROJ
%token<ime> ID
%token PRINT LEQ GEQ NEQ EQ

%type<v> e

%start program

%%

program: program naredba ';'
	| naredba ';'
	;
naredba: PRINT '(' e ')' 	{ printf("Vrednost izraza: %.2f\n", $3); }
	| ID '=' e 		{
						int retVal = pronadji($1);
						if (retVal != -1) {
							
							promenljive[retVal].v = $3;
						}
						else {
						
							promenljive[n].ime = strdup($1);
							if (promenljive[n].ime == NULL) {
							
								fprintf(stderr,"strdup\n");
								exit(EXIT_FAILURE);
							}
							
							promenljive[n].v = $3;
							n++;
							
							if (n == capacity) {
							
								capacity *= STEP;
								
								promenljive = realloc(promenljive, capacity*sizeof(prom_t));
								if (promenljive == NULL) {
								
									fprintf(stderr, "realloc\n");
									exit(EXIT_FAILURE);
								}
							}
						}
						
						free($1);
					}
	| e '<' e		{printf("%s\n", $1 < $3 ? "true" : "false");}
	| e '>' e		{printf("%s\n", $1 > $3 ? "true" : "false");}
	| e LEQ e		{printf("%s\n", $1 <= $3 ? "true" : "false");}
	| e GEQ e		{printf("%s\n", $1 >= $3 ? "true" : "false");}
	| e NEQ e		{printf("%s\n", $1 != $3 ? "true" : "false");}
	| e EQ e		{printf("%s\n", $1 == $3 ? "true" : "false");}
	;
e: e '+' e				{ $$ = $1 + $3; }
 | e '-' e				{ $$ = $1 - $3; }
 | e '*' e				{ $$ = $1 * $3; }
 | e '/' e				{ $$ = $1 / $3; }
 | '(' e ')'			{ $$ = $2;}
 | '-' e %prec UMINUS { $$ = -$2; }
 | BROJ		{ $$ = $1; }
 | ID		{
				int retVal = pronadji($1);
				if (retVal == -1) {
				
					fprintf(stderr, "Nedefinisana promenljiva\n");
					exit(EXIT_FAILURE);
				}
				
				$$ = promenljive[retVal].v;
				
				free($1);
			}
 ;

%%

int main (){
	
	alociraj();

	if (yyparse() == 0) {
	
		printf("Sve ok\n");
	}
	else {
	
		printf("Sintaksna greska\n");
	}
	
	dealociraj();
	
	exit(EXIT_SUCCESS);
}