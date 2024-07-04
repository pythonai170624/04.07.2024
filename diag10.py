## Start

pwd: str = input("what's the password?");

if pwd == "python1234":
    print("correct! you are in!");
else:
    print("wrong! out you go ...");

## more ways to write it:

if not (pwd == "python1234"):
    print("correct! you are in!");
else:
    print("wrong! out you go ...");

if pwd != "python1234":
    print("wrong! out you go ...");
else:
    print("correct! you are in!");

PASSWORD: str = "python1234"
if not (pwd == PASSWORD):
    print("correct! you are in!");
else:
    print("wrong! out you go ...");

## end