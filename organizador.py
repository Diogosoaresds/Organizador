import os
import glob
import shutil

# dicionário mapeando cada extensão com sua pasta correspondente
extensions = {

     "jpg": "imagens",
     "png": "imagens",
     "ico": "imagens",
     "gif": "imagens",
     "svg": "imagens",
     "sql": "sql",
     "exe": "programas",
     "msi": "programas",
     "pdf": "pdf",
     "xlsx": "excel",
     "csv": "excel",
     "rar": "arquivo",
     "zip": "arquivo",
     "gz": "arquivo",
     "tar": "arquivo",
     "docx": "word",
     "torrent": "torrent",
     "txt": "texto",
     "py": "python",
     "pptx": "powerpoint",
     "ppt": "powerpoint",
     "mp3": "audio",
     "wav": "áudio",
     "mp4": "vídeo",
     "m3u8": "vídeo",
     "webm": "vídeo",
     "ts": "vídeo",
     "json": "json",
     "css": "web",
     "js": "web",
     "html": "web",
     "apk": "apk",
     "sqlite3": "sqlite3",
     "rtf": "word",
}

path = r"C:\Users\diogo\Downloads"
    
for extension, folder_name in extensions.items():
    # Pega todos os arquivos que terminam com a extensão
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Encontrados {len(files)} arquivos com extensão '{extension}'")
    
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # Cria a pasta se não existir
        print(f"[+] Making {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
        
    for file in files:
        # Para cada arquivo, move para a pasta correspondente
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        
        print(f"[*] Movendo {file} para {dst}")
        shutil.move(file, dst)
