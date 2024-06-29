
#Problem 1

angka = [2, 3, 3, 3, 6, 9, 9]
set_angka = set(angka)

def remove_duplikat(angka):
    if not angka:
        return 0
    
    next_non_duplikat = 0
    
    for i in range(1, len(angka)):
        if angka[i] != angka[next_non_duplikat]:
            next_non_duplikat += 1
            angka[next_non_duplikat] = angka[i]
    
    return next_non_duplikat + 1


length = remove_duplikat(angka)
print("berapa banyak angka setelah duplikat dihapus:", length)  
print("angka setelah duplikatnya dihapus:", angka[:length])




#Problem 2

def is_prime(num):
    # Fungsi untuk mengecek apakah suatu bilangan prima
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 adalah bilangan prima
    if num % 2 == 0:
        return False  # Bilangan genap selain 2 bukan prima
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primeX(x):
    
    #Fungsi untuk mengembalikan bilangan prima sesuai dengan deret urutannya
    count = 0
    num = 2  # Mulai dari bilangan prima pertama
    while count < x:
        if is_prime(num):
            count += 1
            if count == x:
                return num
        num += 1
    
    # Jika mencapai sini berarti tidak ada hasil, seharusnya tidak terjadi dalam kasus normal
    return None

hasil = primeX(5)
print("urutan ke-5 dari bilangan prima adalah:", hasil)




#Problem 3

def fibonacci(n):
    """ Fungsi untuk menghitung bilangan Fibonacci ke-n """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Inisialisasi dua bilangan pertama dalam deret Fibonacci
    a, b = 0, 1
    
    # Iterasi untuk menghitung nilai Fibonacci ke-n
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    
    return b

result = fibonacci(5)
print("nilai fibonacci-nya adalah:", result)




#Problem 4

def is_prime(num):
    #Fungsi untuk mengecek apakah suatu bilangan prima
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 adalah bilangan prima
    if num % 2 == 0:
        return False  # Bilangan genap selain 2 bukan prima
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prima_persegipanjang(y, x, start_num):
    # Fungsi untuk mencetak persegi panjang berukuran y kali x yang berisi bilangan prima
    count = 0
    num = start_num  # Mulai dari bilangan prima setelah start_num
    for i in range(x):
        for j in range(y):
            while not is_prime(num):
                num += 1
            print(num, end=' ')
            num += 1
        print()  # Pindah baris setelah mencetak satu baris persegi

prima_persegipanjang(2, 3, 13)



#Problem 5

def max_subarray_sum(nums):
    if not nums:
        return 0
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("total maksimumnya adalah:", result)


