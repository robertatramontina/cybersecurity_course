eventos = ["fail", "Ok", "fail", "fail", "ok", "ok"]
falhas = 0

for e in eventos:
    if e == "fail":
        falhas += 1

print(f"Foram detectadas {falhas} falhas de login")