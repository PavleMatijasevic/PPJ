c: lex.yy.c
	gcc lex.yy.c -o c

lex.yy.c: c_komentari.l
	flex c_komentari.l

>PHONY: clean

clean:
	rm -rf lex.yy.c c
