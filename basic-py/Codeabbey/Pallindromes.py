loop = int(input())
status = ''
punct = "''!()-[]{};:'\,<>./?@#$%^&*_~"
for i in range(loop):
    a = ''.join(str(x) for x in input() if x.isalnum())
    a = a.lower()
    b = a[::-1]
    if b == a:
        status += 'Y '
    else:
        status += 'N '
print(status,end=' ')

