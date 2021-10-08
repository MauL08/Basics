kartu = ["CA","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK"
        ,"DA","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK"
        ,"HA","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK"
        ,"SA","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK"]

a = [int(x) for x in input().split()]

for i in range(52):
    a[i] = a[i] % 52
    kartu[i], kartu[a[i]] = kartu[a[i]], kartu[i]

for card in kartu:
    print(card,' ',sep='')