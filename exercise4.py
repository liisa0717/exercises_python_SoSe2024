quad_zahl = []
for zahl in range(1,11):
    if zahl %2 !=0:
        quad_zahl.append(zahl**2)
    else:
        quad_zahl.append(zahl)
        print(quad_zahl)
        
quad_zahl_comprehesnion = [zahl**2 if zahl %2 != 0 else zahl for zahl in range(1,11)]
print(quad_zahl_comprehesnion)
