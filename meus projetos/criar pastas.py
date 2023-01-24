from os import listdir,path,mkdir
pastas=[]
while 'pasta' in listdir(path.abspath('.')+'\\'+'\\'.join(pastas)):pastas.append('pasta')
for pasta in range(1,int(input('quantidade de pastas:'))+1):mkdir(path.abspath('.')+'\\'+'\\'.join(pastas)+'\pasta'*pasta)