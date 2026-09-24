import resources

szo = input("Milyen szót szeretnél ragozni? ")

print()
print(f"-val, -vel:   {resources.ragozas(szo, "val", "vel")}")
print(f"-vá, -vé:   {resources.ragozas(szo, "vá", "vé")}")
print(f"-nak, -nek:   {resources.ragozas(szo, "nak", "nek")}")
print(f"-nál, -nél:   {resources.ragozas(szo, "nál", "nél")}")
print(f"-ra, -re:   {resources.ragozas(szo, "ra", "re")}")