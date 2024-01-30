i = 1
j = 2
k = 3
a = 'a'
b = 'b'
c = 'c'
t = True
f = False

assert (k % 2 == 1) == True
assert (i % 2 != 0) == True
assert (i % 3 >= j % 1) == True
assert (i < j == 2) == True
assert (4 // j > 2 % j) == True

assert (k <= 1 // j) == False
assert (j // 2 == j % 2) == False
assert (3 // j != k % 2) == False
assert (i >= j >= k) == False
assert (i // 2 < 4 % j) == False

assert (4 // i > 0 and 2 <= j // 1) == True
assert (1 > i // j or 3 >= k) == True
assert (i >= 1 and 3 % j != 4) == True
assert (not(3 < j) or 0 < k // 3) == True
assert ((not(k > 1 and 0 == i)) == (not(3 // k < 0) or not(i // 1 >= j))) == True

assert (4 // j < 4 % j and k % 3 != 0) == False
assert (2 * i // j == 0 or (i - 1) != 0) == False
assert (not(2 != 1 // i) and (i + j == k)) == False
assert (not(i >= 1 and k < 4)) == False
assert ((4 < (k * j) and (i > j > k)) == (not(k // 3 != i))) == False
