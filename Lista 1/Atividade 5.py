#Atividade 5 
#Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção, 
#considerando que cada blusa requer uma quantidade de 120 metros de fio e que cada novelo contém 125 de metros de fio?
lã = float(input("insira quantos metros de la você tem: "))
metros_fio = 120
metros_novelos = 125
metros_total = (lã *120) / 125
print(f"são nescessarios: {metros_total} fios de lã para produzir uma blusa" )