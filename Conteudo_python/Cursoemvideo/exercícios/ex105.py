def notas(*n, show=True):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n) / len(n)
    if show:
        if r["média"] >= 7:
            r["situação"] = 'BOA'
        elif r["média"] >= 5:
            r["situação"] = 'RAZOÁVEL'
        else:
            r["situação"] = 'RUIM'
    return r


print(notas(5, 3, 6, 2, 8, 10, show=False))
