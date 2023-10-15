not100, not50, not20, not10, not5, not2 = 0, 0, 0, 0, 0, 0
moe100, moe50, moe25, moe10, moe5, moe1 = 0, 0, 0, 0, 0, 0
val = float(input())
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
    moe100 = val // 1
    val = val - moe100 * 1
if val >= 0.5:
    moe50 = val // 0.5
    val = ((val*100) - (moe50 * 0.5 * 100)) / 100
if val >= 0.25:
    moe25 = val // 0.25
    val = ((val*100) - (moe25 * 0.25 * 100)) / 100
if val >= 0.10:
    moe10 = val // 0.1
    val = ((val*100) - (moe10 * 0.1 * 100)) / 100
if val >= 0.05:
    moe5 = val // 0.05
    val = ((val*100) - (moe5 * 0.05 * 100)) / 100
if val >= 0.01:
    moe1 = val / 0.01
    val = ((val*100) - (moe1 * 0.01 * 100)) / 100
print("NOTAS:")
print(int(not100), "nota(s) de R$ 100.00")
print(int(not50), "nota(s) de R$ 50.00")
print(int(not20), "nota(s) de R$ 20.00")
print(int(not10), "nota(s) de R$ 10.00")
print(int(not5), "nota(s) de R$ 5.00")
print(int(not2), "nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(moe100), "moeda(s) de R$ 1.00")
print(int(moe50), "moeda(s) de R$ 0.50")
print(int(moe25), "moeda(s) de R$ 0.25")
print(int(moe10), "moeda(s) de R$ 0.10")
print(int(moe5), "moeda(s) de R$ 0.05")
print(int(moe1), "moeda(s) de R$ 0.01")
