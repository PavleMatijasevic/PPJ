import sys
import re

poruka = "Danas je dobar dan za setnju drvenim mostovima"
print(poruka)
print("------------------")

matcher = re.match(r'\bd[a-z]+', poruka,re.S | re.I)

if matcher is not None:
    print(matcher.group())

print("------------------")


matcher = re.findall(r'\bd[a-z]+', poruka,re.S | re.I)
if matcher is not None:
    print(matcher)

print("------------------")