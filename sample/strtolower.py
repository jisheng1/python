# -*- coding: utf-8 -*-
# 转小写

def normalize(name):
    return name[:1].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
