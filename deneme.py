a = 121
b = 149
c = 139
fy = 7
points = {a : 0, b  : 0, c : 0}

for i in range (fy):
    big = max(points.keys())
    points[big] += 1
    x = big/2
    points[x] = points.pop(big)
print(points)


# sonuçları buluyor en küçük abc değerleri ile 
# en küçük points değerlerini eşleştirmek gerekiyor


