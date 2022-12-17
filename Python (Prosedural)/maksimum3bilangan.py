# MAKSIMUM 3 BILANGAN
# Membuat program yang membaca 3 buah bilangan integer dan menuliskan
# nilai terbesar di antara ketiganya.

# KAMUS
# l = list

# ALGORITMA
l = [0 for i in range(3)]
for i in range(3):
    l[i] = int(input())
max = l[0]
for i in l:
    if i > max:
        max = i
print(max)