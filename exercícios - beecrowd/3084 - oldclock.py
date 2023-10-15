while True:
    try:
        h, m= map(int, input().split())
        h = h // 30
        m = m // 6
        print("{:0>2}:{:0>2}".format(h, m))
    except EOFError:
        break