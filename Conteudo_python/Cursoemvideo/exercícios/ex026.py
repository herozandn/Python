p = str(input("Digite uma frase: ")).lower().strip()
print("A letra 'a' aparece {} vezes"
      "\nEla aparece primeiro na posição {}"
      "\nEla aparece por último na posição {}".format(p.count("a"), p.find("a")+1, p.rfind("a")+1))
