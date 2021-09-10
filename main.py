import sys
from string import printable

alphabets = list(printable)
string_input = open("zeroarquivo.txt", 'r' , encoding='utf-8')
f = str(string_input.read())
key = 3
string_output = ""
a = int(input("Digite 1:"))

if a == 1:
    print("\nSeus dados foram criptografados. Contate-nos para tê-los de volta.")
    for i in f:
        if i in alphabets:
            pos = alphabets.index(i)
            new_location = (pos - key) % 100
            string_output += alphabets[new_location]
        print(string_output)
    string_input.close()
    cripto = open('C:/Users/T-Gamer/PycharmProjects/pythonProject/zeroarquivo.txt' , 'w', encoding='utf-8')
    cripto.writelines(string_output)
    cripto.close


else:
    string_input = open("zeroarquivo.txt", 'r', encoding='utf-8')
    decript = str(string_input.read())
    descript = ""
    print(decript)
    for i in decript:
        if i in alphabets:
            pos = alphabets.index(i)
            new_location = (pos + key) % 100
            descript += alphabets[new_location]
        print(descript)
    decript = open('C:/Users/T-Gamer/PycharmProjects/pythonProject/zeroarquivo.txt', 'w', encoding='utf-8')
    decript.writelines(descript)
    decript.close
