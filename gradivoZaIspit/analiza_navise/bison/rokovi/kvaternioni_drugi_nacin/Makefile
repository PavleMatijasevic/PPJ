parser: lexer.o parser.o
	g++ -std=c++11 lexer.o parser.o -o parser

parser.o: parser.tab.cpp parser.tab.hpp
	g++ -std=c++11 -c parser.tab.cpp -o parser.o

lexer.o: lex.yy.c
	g++ -std=c++11 -c lex.yy.c -o lexer.o

lex.yy.c: lexer.l parser.tab.hpp kvaternion.hpp
	flex lexer.l

parser.tab.cpp parser.tab.hpp: parser.ypp kvaternion.hpp
	bison -d -v parser.ypp

.PHONY: clean

clean:
	rm -rf *.o *.output *.tab.* *.yy.* parser