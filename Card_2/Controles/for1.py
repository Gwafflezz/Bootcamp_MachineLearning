
for i in range(10):
    print(i, end='')
    print('')

for i in range(1,11):
    print(i, end='')
print('')
for i in range(1,100,7):
    print(i, end='') 
print('')
for i in range(20,0,-3):
    print(i, end='') 
print('')
nums = [2,4,6,8]

for n in nums:
    print(n, end = '')
print('')

texto = 'python e mt massa'

for letra in texto:
    print(letra, end='')
print('')

for n in {1, 2, 2, 3, 4, 4 }:
    print(n, end ='')
print('')
 
produto = {

    'nome': 'caneta',
    'preco': 8.00,
    'desconto': 0.5,

}

for atrib in produto:
    print(atrib, '=' ,produto[atrib])
print('')

for atrib, valor in produto.items():
    print(atrib, '=' ,valor , end=', ')

print('')

for  valor in produto.values():
    print(valor, end=', ')
print('')

for atrib in produto.keys():
        print(atrib, end= ', ')
print('')
          