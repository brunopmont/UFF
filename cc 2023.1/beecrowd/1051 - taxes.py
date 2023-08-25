sal = float(input())
tax = 0
tax8 = 0
tax18 = 0
tax28 = 0
if sal <= 2000:
    print("Isento")
else: 
    if sal > 4500:
        tax28 = (sal - 4500) * 0.28
        tax18 = 1500 * 0.18
        tax8 = 1000 * 0.08
    elif 3000 < sal <= 4500:
        tax28 = 0
        tax18 = (sal - 3000) * 0.18
        tax8 = 1000 * 0.08
    elif 2000 < sal <= 3000:
        tax28 = 0
        tax18 = 0
        tax8 = (sal - 2000) * 0.08
    print("R$ {:.2f}".format(tax28 + tax18 + tax8))