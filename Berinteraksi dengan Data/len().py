#len()
#Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.
#Khusus pada string, program akan menghitung jumlah karakternya.

contoh_list = [1,3,5,2,3,5,2,5,2,4,2,2,0,1,3,3]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 5, 2, 3, 5, 2, 5, 2, 4, 2, 2, 0, 1, 3, 3]
16
"""

contoh_list = set([1,3,5,2,3,5,2,5,2,4,2,2,0,1,3,3])

print(contoh_list)
print(len(contoh_list))

"""
Output:
{0, 1, 2, 3, 4, 5}
6
"""

contoh_list = "Belajar Python"
print(contoh_list)
print(len(contoh_list))


"""
Output:
Belajar Python
14
"""
