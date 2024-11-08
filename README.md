# TutorIA: Assistente de Estudo para Crianças

Este projeto implementa uma inteligência artificial (IA) conversacional projetada para auxiliar crianças de 6 anos em seus estudos, adotando uma abordagem pedagógica que incentiva o pensamento crítico, a autodescoberta e a reflexão. O TutorIA interage com a criança de maneira amigável e paciente, fornecendo dicas e encorajamento antes de revelar a resposta correta.

## Estrutura do Projeto

- **ai.py**: Define o modelo de IA com uma personalidade tutora e métodos de ensino apropriados para crianças. Inclui um prompt detalhado e uma cadeia de LLM (Large Language Model) para gerenciar as interações.
- **voice.py**: Utiliza a API ElevenLabs para gerar e reproduzir a resposta de voz do TutorIA.
- **app.py**: Cria uma interface web com Flask, permitindo que o usuário interaja com o TutorIA por meio de entrada de texto ou áudio.

## Requisitos

Certifique-se de ter os seguintes pacotes e dependências instalados para executar o projeto:

- **Python** (>=3.8)
- **Bibliotecas Python**:
  - `langchain_community`
  - `dotenv`
  - `flask`
  - `speech_recognition`
  - `pydub`
  - `psutil`
  - `webbrowser`
- **ffmpeg**: Necessário para conversão de arquivos de áudio. [Instruções de instalação](https://ffmpeg.org/download.html).
- **ElevenLabs API**: Para a reprodução de voz, crie uma conta em [ElevenLabs](https://www.elevenlabs.io/) e obtenha uma chave de API.

Lembre-se de criar o arquivo .end e incluir as chaves da OpenAi e ElevenLabs.
Exemplo:
   OPENAI_API_KEY = "xxxxx"
   ELEVEN_LABS_API_KEY = "xxxxx"-

## Configuração

1. **Instalação das Dependências**: Use o comando abaixo para instalar as dependências do Python:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuração das Variáveis de Ambiente**: Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do ElevenLabs:
   ```
   ELEVEN_LABS_API_KEY=seu_api_key_aqui
   ```

3. **FFmpeg**: Instale o ffmpeg e certifique-se de que ele esteja no PATH do sistema. Exemplo de instalação no Ubuntu:
   ```bash
   sudo apt-get install ffmpeg
   ```

## Uso

1. Execute o aplicativo Flask:
   ```bash
   python app.py
   ```

2. Acesse a interface do TutorIA no navegador em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Interação**: Você pode interagir com o TutorIA usando texto ou enviando um arquivo de áudio.

## Funcionalidades

- **Interface Amigável**: O TutorIA fornece dicas antes de dar a resposta correta, incentivando a criança a pensar por conta própria.
- **Feedback de Voz**: As respostas da IA são lidas em voz alta para criar uma experiência de aprendizado mais envolvente.
- **Suporte a Áudio**: Aceita entrada de voz e converte o áudio em texto para a IA responder.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o TutorIA. 
