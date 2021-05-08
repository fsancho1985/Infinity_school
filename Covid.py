sintomasLeves = 0
assintomaticos = 0
sintomasGraves = 0
sintoma = 0

for i in range(10):
    sintomas = input("Qual o nível de sintoma do paciente? ")
    if sintoma == "leve":
        sintomasLeves += 1
        print(sintomasLeves)
    if sintoma == "assintomático":
        assintomaticos += 1
        print(assintomaticos)
    if sintoma == "grave":
        sintomasGraves +=1
        print(sintomasGraves)

percLeves = (sintomasLeves / 10)*100
percassint = (assintomaticos / 10)*100
percGraves = (sintomasGraves / 10)*100
print(percLeves)
print(percassint)
print(percGraves)
