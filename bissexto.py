num = int(input())
if num % 4 == 0 and num % 100 != 0 or num % 100 == 0 and num % 400 == 0:
    print('{} é bissexto'.format(num))
else:
    print('{} não é bissexto'.format(num))