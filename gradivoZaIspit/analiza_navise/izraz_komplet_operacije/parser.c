#include <stdio.h>
#include <stdlib.h>
#include "tokeni.h"

extern int yylex();
int yylval = 0;
int preduvid = 0;

int e();
int ep(int nasledjen);
int t();
int tp(int nasledjen);
int f();

int main(){
	
	preduvid = yylex();
	
	int rez = e();
	
	if (preduvid == EOI) {
		
		printf("Vrednost izraza: %d\n", rez);
	}
	else {
		
		printf("Sintaksna greska. Visak tokena na ulazu\n");
	}
	
	exit(EXIT_SUCCESS);
}

int e() {
	
	if (preduvid == OZ || preduvid == BROJ) {
		
		int nasledjen = t();
		return ep(nasledjen);
	}
	else {
		
		fprintf(stderr, "Sintaksna greska\n");
		exit(EXIT_FAILURE);
	}
}

int ep(int nasledjen) {
	
	if (preduvid == PLUS) {
		
		preduvid = yylex();
		int rez = nasledjen + t();
		return ep(rez);
	}
	else if (preduvid == MINUS) {
		
		preduvid = yylex();
		int rez = nasledjen - t();
		return ep(rez);
	}
	else if (preduvid == ZZ || preduvid == EOI) {
		
		return nasledjen;
	}
	else {
		
		fprintf(stderr, "Sintaksna greska\n");
		exit(EXIT_FAILURE);
	}
}

int t() {
	
	if (preduvid == OZ || preduvid == BROJ) {
		
		int nasledjen = f();
		return tp(nasledjen);
	}
	else {
		
		fprintf(stderr, "Sintaksna greska\n");
		exit(EXIT_FAILURE);
	}
}

int tp(int nasledjen) {
	
	if (preduvid == PUTA) {
	
		preduvid = yylex();
		int rez = nasledjen * f();
		return tp(rez);
	}
	else if (preduvid == PODELJENO) {
		
		preduvid = yylex();
		int rez = nasledjen / f();
		return tp(rez);
	}
	else if (preduvid == MINUS || preduvid == PLUS || preduvid == ZZ || preduvid == EOI) {
		
		return nasledjen;
	}
	else {
		
		fprintf(stderr, "Sintaksna greska\n");
		exit(EXIT_FAILURE);
	}
}

int f() {
	
	if (preduvid == BROJ) {
	
		int rez = yylval;
		preduvid = yylex();
		return rez;
	}
	else if (preduvid == OZ){
		
		preduvid = yylex();
		int rez = e();
		
		if (preduvid != ZZ) {
			
			fprintf(stderr, "Sintaksna greska\n");
			exit(EXIT_FAILURE);
		}
		
		preduvid = yylex();
		
		return rez;
	}
	else {
		
		fprintf(stderr, "Sintaksna greska\n");
		exit(EXIT_FAILURE);
	}
}

