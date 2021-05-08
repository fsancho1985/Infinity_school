leves = 0
graves = 0
assint = 0

for i in range(10):
    classificacao = input("Qual o grau de sintoma? ")
    if classificacao == "leve":
        leves += 1
        print(leves)
    elif classificacao == "grave":
        graves += 1
        print(graves)
    elif classificacao == "assintomatico":
        assint += 1
        print(assint)
        
percLeves = (leves / 10)*100
percGraves = (graves / 10)*100
percAssint = (assint / 10)*100

print(percLeves,"%")
print(percGraves,"%")
print(percAssint,"%")
