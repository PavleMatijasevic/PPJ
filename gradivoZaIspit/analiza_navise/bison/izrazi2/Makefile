parser: parser.o lexer.o
	gcc parser.o lexer.o -o parser

lexer.o: lex.yy.c
	gcc -c lex.yy.c -o lexer.o

parser.o: parser.tab.c parser.tab.h
	gcc -c parser.tab.c -o parser.o

lex.yy.c: lexer.l parser.tab.h
	flex lexer.l

parser.tab.c parser.tab.h: parser.y
	bison -d -v parser.y


.PHONY: clean

clean:
	rm -rf parser *.o *.tab.* *.yy.* *.outp
