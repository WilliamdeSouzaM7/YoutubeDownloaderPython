# YouTube Downloader - Debian 12
Um script Python para baixar vídeos, áudios ou playlists do YouTube em um ambiente isolado/virtualizado.

## Pré-requisitos

- Debian 12 (ou qualquer distribuição Linux)
- Python 3.10 ou superior
- `pip` (gerenciador de pacotes Python)
- `venv` (módulo padrão do Python para ambientes virtuais)

## Instalação

### 1. Criar ambiente virtual isolado

```bash
# Criar diretório para o projeto
mkdir youtube-downloader && cd youtube-downloader

# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate
```

### 2. Instalar dependências

```bash
# Instalar pytube (biblioteca para download do YouTube)
pip install pytube
```


## Uso
### Executar o script

```bash
# Certifique-se de estar no diretório do projeto e com o ambiente virtual ativado
source venv/bin/activate

# Executar o script
python youtube\_downloader.py

```

### Opções disponíveis
Ao executar o script, você verá as seguintes opções:

```bash
Choose what you want to download:
"s" => Single video
"a" => Audio
"l" => Playlist
```

Digite a opção desejada e siga as instruções:
- Single video (s): Baixa um vídeo específico
- Audio (a): Baixa apenas o áudio do vídeo
- Playlist (l): Baixa todos os vídeos de uma playlist

## Exemplo de Uso

```bash
# Baixar um vídeo
python youtube\_downloader.py
# Digite "s" quando solicitado
# Cole a URL do vídeo quando solicitado

# Baixar áudio
python youtube\_downloader.py
# Digite "a" quando solicitado
# Cole a URL do vídeo quando solicitado

# Baixar playlist
python youtube\_downloader.py
# Digite "l" quando solicitado
# Cole a URL da playlist quando solicitado
```

## Estrutura do projeto

```bash
youtube-downloader/
├── venv/               # Ambiente virtual Python
├── youtube\_downloader.py # Script principal
└── README.md           # Este arquivo
```

## Notas importantes
- Diretório de saída: Os downloads serão salvos em ~/Downloads/Video (pasta criada automaticamente se não existir)

### Formato dos arquivos:
- Vídeos: Formato padrão do YouTube (geralmente MP4)
- Áudios: Formato padrão do YouTube (geralmente M4A)
- Resolução: O script baixa a maior resolução disponível
- Isolamento: Todo o ambiente é isolado no diretório venv, não afetando outros projetos Python

### Desativar o ambiente virtual
Quando terminar de usar o script, desative o ambiente virtual com:

```bash
deactivate
```
### Solução de problemas
Se encontrar erros:
- Verifique se o ambiente virtual está ativado (venv/bin/activate)
- Verifique se todas as dependências estão instaladas (pip list)
- Verifique sua conexão com a internet
- Tente atualizar o pytube: pip install --upgrade pytube

## Licença
Este projeto é de código aberto e pode ser usado livremente.
