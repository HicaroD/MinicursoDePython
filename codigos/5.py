agenda_telefonica = {"Roberto": 128331239, "Rebeca": 129391391312}
agenda_telefonica["Hicaro"] = 12023817845750653

del agenda_telefonica["Hicaro"]

for chave, valor in agenda_telefonica.items():
    print(chave + "--->" + str(valor))

print(agenda_telefonica["Hicaro"])