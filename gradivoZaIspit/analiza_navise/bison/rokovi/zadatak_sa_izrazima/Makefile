parser: parser.o lexer.o broj.o
	g++ -std=c++11 parser.o lexer.o broj.o -o parser

broj.o: broj.cpp broj.hpp
	g++ -std=c++11 -c broj.cpp -o broj.o

parser.o: parser.tab.cpp parser.tab.hpp
	g++ -std=c++11 -c parser.tab.cpp -o parser.o

lexer.o: lex.yy.c
	g++ -std=c++11 -c lex.yy.c -o lexer.o

lex.yy.c: lexer.l parser.tab.hpp	
	flex lexer.l

parser.tab.hpp parser.tab.cpp: parser.ypp
	bison -d -v parser.ypp

.PHONY: clean

clean: 
	rm -rf parser *.tab.* *.yy.* *.o *.output