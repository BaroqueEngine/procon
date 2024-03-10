T = "tourist 3858\n"\
    "ksun48 3679\n"\
    "Benq 3658\n"\
    "Um_nik 3648\n"\
    "apiad 3638\n"\
    "Stonefeang 3630\n"\
    "ecnerwala 3613\n"\
    "mnbvmar 3555\n"\
    "newbiedmy 3516\n"\
    "semiexp 3481"\

dic = {}
for t in T.split("\n"):
    name, rate = t.split()
    dic[name] = rate

print(dic[input()])
