import os, subprocess, sys


pasta= input('insira o caminho:')
print('entrando no loop')
for diretorio, subpastas, arquivos in os.walk(pasta):
	for arquivo in arquivos:
		#print(os.path.join(diretorio, arquivo)) para checar se o caminho indicado está correto
		caminho = diretorio + arquivo
		nome_base = os.path.basename(caminho)
		quebra = nome_base.split('.')
		nome = quebra[0]
		saida = '/home/lab/Desktop/Dados/Layla/repeticao-art_illumina/saida_individuos_vs/' + nome + '_'
		dados = '/home/lab/Desktop/Dados/Layla/art_illumina -ss HS25 -i ' + caminho + ' -p -l 150 -f 30 -m 450 -s 150 -na -o ' + saida
		#print(dados) 
		os.system(dados)				
		#break

		
		
		

