p1 = float(input("Ethics: "))
p2 = float(input("Understanding the Self: "))
p3 = float(input("Mathematics in the Modern World: "))

average = (p1 + p2 + p3) / 3

print("AVERAGE : " + str(average))

if average > 100 or average <= 50:
    print("INVALID GRADE")
elif average >= 98:
    print("WITH HIGHES HONOR")
elif average >= 95:
    print("WITH HIGH HONOR")
elif average >= 90:
    print("WITH HONOR")
elif average >= 75:
    print("PASSED")
else:
    print("FAILED")
