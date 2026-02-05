#1
def jadval(son):
    for i in range(1, 11):
        print(f"{son} * {i} = {son * i}")


jadval(12)


# 2
def kvadrat(royxat):
    new_r = []
    for i in royxat:
        new_r.append(i ** 2)

    print(new_r)


royxat = [12, 8, 9, 4, 6]
kvadrat(royxat)


# 4
def malumot(ism, familiya, yosh):
    print(f"Ismi : {ism} \nfamiliyasi : {familiya} \nyoshi : {yosh}")


malumot("Tom", "Jack", 12)


# 5
def bolish(start, end):
    for i in range(start, end):
        if i % 5:
            print(i)


bolish(10, 60)
