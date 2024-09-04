a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

if a<b<c:
    print(f" {a}\n {b}\n {c}\n")

if a<c<b:
    print(f" {a}\n {c}\n {b}\n")

if b<c<a:
    print(f" {b}\n {c}\n {a}\n")

if b<a<c:
    print(f" {b}\n {a}\n {c}\n")

if c<a<b:
    print(f" {c}\n {a}\n {b}\n")

if c<b<a:
    print(f" {c}\n {b}\n {a}\n")