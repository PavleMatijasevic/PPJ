paskal: lex.yy.c
	gcc lex.yy.c -o paskal

lex.yy.c: paskal.l
	flex paskal.l

>PHONY: clean

clean:
	rm -rf lex.yy.c paskal
