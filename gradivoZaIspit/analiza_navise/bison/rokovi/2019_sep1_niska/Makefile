parser: parser.o lexer.o
	g++ -std=c++11 parser.o lexer.o -o parser
lexer.o: lex.yy.c
	g++ -std=c++11 -c lex.yy.c -o lexer.o
parser.o: parser.tab.hpp parser.tab.cpp
	g++ -std=c++11 -c parser.tab.cpp -o parser.o
lex.yy.c: lexer.l parser.tab.hpp
	flex lexer.l
parser.tab.hpp parser.tab.cpp: parser.ypp
	bison -d -v parser.ypp

.PHONY:clean
clean:
	rm -rf *.o *.output *.yy.* *.tab.* parser