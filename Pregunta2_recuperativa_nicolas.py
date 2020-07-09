def convert_to_mandarin(num):
    trans = {'0':'ling', '1':'yi','2':'er','3':'san','4':'si',
        '5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','10':'shi'
        }
    if 10<int(num) and num[1]=='0':
        val = trans[num[0]]+' '+trans['10']
    elif 19<int(num):
        val = trans[num[0]]+' '+trans['10']+' ' +trans[num[1]]
    elif 10<int(num):
        val = trans['10']+' '+trans[num[1]]
    else:
        val = trans[num]
    return val

num  = input('Ingrese un número menor a 100 :')
chin = convert_to_mandarin(num)
print(chin)
    