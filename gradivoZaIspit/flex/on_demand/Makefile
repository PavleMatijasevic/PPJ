on_demand: lex.yy.c
	gcc lex.yy.c -o on_demand

lex.yy.c: on_demand.l
	flex on_demand.l

>PHONY: clean

clean:
	rm -rf lex.yy.c on_demand
