t = ("Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Bragantino", "Athlético-PR", "Fluminense", "Cuiabá", "São Paulo",
     "Atlético-MG", "Fortaleza", "Cruzeiro", "Internacional", "Corinthians", "Goiás", "Bahia", "Santos", "Coritiba",
     "Vasco", "América-MG")

print(f"Os cinco primeiros colocados são: {t[0:5]}")
print("-="*50)
print(f"Os quatro últimos colocados são: {t[-4:]}")
print("-="*50)
print(sorted(t))
print("-="*50)
print(f"A Chapecoense está na {t.index('Chapecoense')}ª posição"
      if "Chapecoense" in t else "A Chapecoense não está em nenhuma posição")
