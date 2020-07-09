def convert_to_mandarin(num):
    trans = {'0':'ling', '1':'yi','2':'er','3':'san','4':'si',
        '5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','10':'shi'
        }
    decena = ' '+trans['10']+' ' 
    if int(num)<= 10:
        chino = trans[num]
    elif int(num)<=19:
        chino = decena+trans[num[1]]
    elif int(num)<=99 and num[1]!='0':
        chino = trans[num[0]]+decena+trans[num[1]]
    else:
        chino = trans[num[0]]+decena
    return chino

numeros = ['36','20','16']
for numero in numeros:
    print(convert_to_mandarin(numero))