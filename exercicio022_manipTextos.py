#Criar programa p/ ler nome completo e mostre: 
# 1) c/ todas letras maiúsculas;
# 2) c/ todas letras minúsculas; 
# 3) Qntas letras tem ao todo sem considerar o 'espaços'; 
# 4) qntas letars tem o 1º nome.

  
nome = str(input('Digite seu nome completo: ')).strip()  #strip p/ eliminar espaços antes e depois do nome

print("O nome com todas as letras em maiúsculo é: ", nome.upper())
print("O nome com todas as letras em minúsculo é: ", nome.lower())
print("Seu nome tem ao todo ", len(nome) - nome.count(" "), "letras.")

print("O primeiro nome tem ", len(nome.split()[0]), "letras.")
