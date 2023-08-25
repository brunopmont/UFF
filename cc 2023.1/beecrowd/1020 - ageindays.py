itd = int(input())
print("{} ano(s)".format(itd // 365))
print("{} mes(es)".format((itd % 365) // 30))
print("{} dia(s)".format((itd % 365) % 30))
