parser: parser.o lex.yy.o
	gcc parser.o lex.yy.o -o parser

parser.o: parser.c tokeni.h
	gcc -c parser.c -o parser.o

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c -o lex.yy.o

lex.yy.c: lekser.l tokeni.h
	flex lekser.l

.PHONY: clean

clean:
	rm -rf parser *.yy.* *.o
