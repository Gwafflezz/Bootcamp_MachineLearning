lockdown = True
grana = 130 

status = ' em casa ' if lockdown and grana <= 100 else ' uhuu ' 

print(f' o status é: {status}') 
