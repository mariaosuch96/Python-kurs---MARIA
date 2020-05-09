# ZAD 1. tuple, listy, zbiory, słowniki
# ZAD 2. słownik, lista
# ZAD 3.
lista = [16, 21, 9, 2, 0, 3, 1]
for indeks_podstawienia in range(len(lista)):
    minValue = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
        if lista(indeks_ogona) < lista(minValue):
            minValue = indeks_ogona

    lista(indeks_podstawienia), lista(minValue) = lista(minValue), lista(indeks_podstawienia)

print(lista)
assert lista == [0, 1, 2, 3, 9, 16, 21]

# ZAD 4.
zrodla = {"a": 10, "b":30}

if "c" in zrodla:
    print(zrodla["c"])
else:
    print("NONE")

# ZAD 5.
def foo(*args, **kwargs):
    print("argumenty pozycyjne: ", len(args))
    print("argumenty kluczowe: ", len(kwargs))

foo(10, 20, a=1, b=2, c=3)
