import os
from config import*
def recupera_imagem(id):
    for nome_arquivo in os.listdir(upload_img):
        if f'{id}' in nome_arquivo:#verifica se img na pasta
            return nome_arquivo
        
        
    return'foto.jpg'

def deleta_img(id):#essa funçao deleta img dentro pasta
    arquivo=recupera_imagem(id)
    print(id)
    os.remove(os.path.join(upload_img, arquivo)) 
    #if arquivo !='foto.jpg':