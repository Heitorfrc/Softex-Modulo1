'''
Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum
candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve
retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a
quantidade de votos de cada candidato, os brancos e nulos 

'''

x = 0
y = 0
z = 0
n = 0

def imprime_opcoes():
    print ("O número do candidato X é 889")
    print ("O número do candidato Y é 847")
    print ("O número do candidato Z é 515")
    print ("Para branco vote 0, para nulo vote em quaisquer outro número")

while True :
    try :
        imprime_opcoes()
        voto = int(input("Digite o número do candidato do seu voto: "))
        if voto == 889 :
            x += 1      
        elif voto == 847 :
            y += 1
        elif voto == 515 :
            z += 1
        else :
            n += 1
                
        encerrar = str(input("Aperte x para encerrar a votação, ou qualquer outra tecla para continuar: "))
        if encerrar == "x" :
            break
    except :
        print("Erro, utilize números para votar")

v = max(x,y,z,n)
if v == x and x != y and x != z and x != n:
    print("O vencedor foi o Candidato X")
elif v == y and y != x and y != z and y != n:
    print("O vencedor foi o Candidato Y")
elif v == z and z != x and z != y and z != n:
    print("O vencedor foi o Candidato Z")
elif v == n and n != x and n != y and n != z:
    print("Os votos brancos e nulos foram a maioria dos votos")
else :
    print("A eleição terminou empatada")


print("O Candidato X ficou com", x, "votos.")
print("O Candidato Y ficou com", y, "votos.")
print("O Candidato Z ficou com", z, "votos.")
print("Os brancos e nulos ficaram com", n, "votos.")
