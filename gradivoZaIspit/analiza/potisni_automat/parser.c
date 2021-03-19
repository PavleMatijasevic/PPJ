/* E -> T EP			(, BROJ
 * TP -> + T EP			+
 * 		eps				), EOI
 * T -> F TP			(, BROJ
 * TP -> * F TP			*
 *      eps				+, ZZ, EOI
 * F -> ( E )			(
 * 		BROJ			BROJ
 */
#include <stdio.h>
#include <stdlib.h>

#include "tokeni.h"

#define MAX_DEPTH (256)

extern int yylex();

int stek[MAX_DEPTH];
int sp = 0;

void push(int x);
int pop(void);
int peek(void);
	
int check(int x);
int empty(void);

int main(int argc, char** argv) {
	
	int preduvid = yylex();
	
	push(E);
	
	while (!empty()) {
		
		switch (peek()) {
			
			case E:
				if (preduvid == OZ || preduvid == BROJ) {
					pop();
					push(EP);
					push(T);
				}
				else {
					check_error(0,"");
				}
				break;
			case EP:
				if (preduvid == PLUS) {
					pop();
					push(EP);
					push(T);
					push(PLUS);
				}
				else if (preduvid == ZZ || preduvid == EOI){
					
					pop();
				}
				else {
					check_error(0,"");
				}
				break;
			case T:
				if (preduvid == BROJ || preduvid == OZ) {
					pop();
					push(TP);
					push(F);
				}
				else {
					check_error(0,"");
				}
				break;
			case TP:
				if (preduvid == PUTA) {
					
					pop();
					push(TP);
					push(F);
					push(PUTA);
				}
				else if (preduvid == PLUS || preduvid == ZZ || preduvid == EOI) {
						
					pop();
				}
				else {
					check_error(0,"");
				}
				break;
			case F:
				if (preduvid == OZ) {
					pop();
					push(ZZ);
					push(E);
					push(OZ);
				}
				else if (preduvid == BROJ) {
						
					pop();
					push(BROJ);
				}
				else {
					check_error(0,"");
				}
				break;
			default:
				if (check(preduvid)) {
					
					pop();
					preduvid = yylex();
				}
				else {
					check_error(0,"");
				}
				break;
		}
	}
	
	printf("Sve ok\n");
	
	exit(EXIT_SUCCESS);
}

void push(int x) {
	
	check_error(sp < MAX_DEPTH, "pun stek");
	
	stek[sp++] = x;
}

int pop(void) {
	
	check_error(sp > 0, "prazan stek");
	
	return stek[--sp];	
}

int peek(void) {
	
	check_error(sp > 0, "prazan stek");
	
	return stek[sp - 1];
}

int check(int x) {
	
	check_error(sp > 0, "prazan stek");
	
	return stek[sp-1] == x;
}

int empty(void) {
	
	return sp == 0;
}
