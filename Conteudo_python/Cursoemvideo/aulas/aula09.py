frase = "Curso em Vídeo Python"
print(frase[9::3])
print(len(frase))
# comprimento da variável
print(frase.upper().count("O"))
# conta quantas vezes o argumento aparece
print(frase.count("o", 0, 13))
# faz a mesma coisa, só que com fatiamento
print(frase.find("deo"))
# em que posição o argumento começa
print("Curso" in frase)
# diz se existe o argumento na variável
print(frase.replace("Python", "Android"))
# substitui o argumento na variável
print(frase.upper())
# todos os caracteres maiúsculos
print(frase.lower())
# todos os caracteres minúsculos
print(frase.capitalize())
# só o primeiro caracter fica maiúsculo
print(frase.title())
# o primeiro caracter de cada palavra fica maiúsculo
print("----------------------------------------------------------------------------------------------------------------")
frase_2 = "   Aprenda Python  "
print(frase_2.strip())
# remove os espaços redundantes
print(frase_2.rstrip())
# remove somente os espaços da direita
print(frase_2.lstrip())
# remove somente os espaços da esquerda
print("----------------------------------------------------------------------------------------------------------------")
a = frase.split()
print(a[0:2])
# divisão dentro da variável considerando os espaços
print("".join(a))
# junta as variáveis levando em consideração o separador
