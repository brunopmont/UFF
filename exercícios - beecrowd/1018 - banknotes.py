not100 = 0
not50 = 0
not20 = 0
not10 = 0
not5 = 0
not2 = 0
not1 = 0
val = int(input())
print(val)
if val >= 100:
    not100 = val // 100
    val = val - not100 * 100
if val >= 50:
    not50 = val // 50
    val = val - not50 * 50
if val >= 20:
    not20 = val // 20
    val = val - not20 * 20
if val >= 10:
    not10 = val // 10
    val = val - not10 * 10
if val >= 5:
    not5 = val // 5
    val = val - not5 * 5
if val >= 2:
    not2 = val // 2
    val = val - not2 * 2
if val >= 1:
    not1 = val // 1
    val = val - not1 * 1
print(not100, "nota(s) de R$ 100,00")
print(not50, "nota(s) de R$ 50,00")
print(not20, "nota(s) de R$ 20,00")
print(not10, "nota(s) de R$ 10,00")
print(not5, "nota(s) de R$ 5,00")
print(not2, "nota(s) de R$ 2,00")
print(not1, "nota(s) de R$ 1,00")