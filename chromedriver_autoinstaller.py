import requests # Biblioteca utilizada para fazer requests a urls
import platform # 
import zipfile  # Biblioteca utilizada para interagir com arquivos .zip
import os       # Biblioteca utilizada para interagir com o sistema operacional 

def download_chromedriver(destiny: str, disk: str = "C:\\") -> str:
    # Identifica sistema operacional
    os_name = platform.system()
    if(os_name == "Windows"):
        bar = "\\"
        # Coleta do path do chrome.exe
        for root, dirs, files in os.walk(disk):                                                             # Olha os arquivos e pastas que estão no disco "disk"
            if 'chrome.exe' in files:                                                                       # Verifica se o chrome.exe está entre eles
                chromePath = os.path.join(root, 'chrome.exe').replace(bar,bar*2)                            # Converte as barras individuais em barras duplas para o python poder ler                      
                break                                                                                       # Encerra a procura
        
        # Coleta de versão
        chromeVersion = os.popen(f"wmic datafile where name='{chromePath}' get Version /value")             # Busca pela versão atual do chrome.exe no terminal por meio do path dele no windows
        chromeVersion = chromeVersion.read().replace("Version=","").replace("\n","")                        # Lê o resultado do comando anterior e retira os espaços vazios e outras informações desnecessárias
    
    elif(os_name == "Linux"):
        bar = "/"
        chromeVersion = os.popen('google-chrome --version | grep -iE "[0-9.]{10,20}"')                      # Retorna a versão do Google chrome

    # Etapa de download
    downloadLink = f"https://chromedriver.storage.googleapis.com/{chromeVersion}/chromedriver_win32.zip"    # Abre o link de download do chromedriver
    downloadLink = requests.get(downloadLink)                                                               # Abre o link de download do chromedriver

    # Etapa de download e extração
    open(f"{destiny}{bar}chromedriver.zip",'wb').write(downloadLink.content)                                # Baixa o conteúdo da página de download no local "destiny"
    with zipfile.ZipFile(f"{destiny}{bar}chromedriver.zip", 'r') as zip_ref:                                # Abre o arquivo com terminação .zip em modo de leitura
        zip_ref.extractall(destiny)                                                                         # Extrai o conteúdo do arquivo para o local "destiny"
    
    # Retorno do local do chromedriver.exe
    return destiny + f"{bar}chromedriver.exe"                                                                   

if __name__ == "__main__":
    download_chromedriver(os.getcwdb().decode("utf-8"))