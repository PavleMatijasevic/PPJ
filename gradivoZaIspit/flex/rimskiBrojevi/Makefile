rimski: lex.yy.c
	gcc lex.yy.c -o rimski

lex.yy.c: rimski.l
	flex rimski.l

>PHONY: clean

clean:
	rm -rf lex.yy.c rimski
