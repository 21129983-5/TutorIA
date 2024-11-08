from ai import get_response_from_ai
from flask import Flask, render_template, request
import speech_recognition as sr
from pydub import AudioSegment
import os
import webbrowser
import threading
import sys
import psutil
from werkzeug.utils import secure_filename

app = Flask(__name__)

browser_process = None  # Variável global para armazenar o processo do navegador

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    human_input = None

    # Primeiro verifica se um arquivo de áudio foi enviado
    if 'audio_input' in request.files and request.files['audio_input'].filename != '':
        audio_file = request.files['audio_input']
        filename = secure_filename(audio_file.filename)
        original_audio_path = os.path.join("temp", filename)
        audio_file.save(original_audio_path)

        # Converte o áudio para WAV usando pydub
        converted_audio_path = os.path.join("temp", "converted_audio.wav")
        try:
            audio = AudioSegment.from_file(original_audio_path)
            audio.export(converted_audio_path, format="wav")
        except Exception as e:
            return f"Erro ao converter o áudio: {str(e)}"

        # Utiliza a biblioteca SpeechRecognition para converter o áudio em texto
        recognizer = sr.Recognizer()
        with sr.AudioFile(converted_audio_path) as source:
            audio_data = recognizer.record(source)
            try:
                human_input = recognizer.recognize_google(audio_data, language="pt-BR")
            except sr.UnknownValueError:
                return "Não foi possível entender o áudio."
            except sr.RequestError:
                return "Erro ao conectar com o serviço de reconhecimento de fala."

        # Remove os arquivos temporários após a conversão
        os.remove(original_audio_path)
        os.remove(converted_audio_path)

    # Caso o campo de texto tenha sido preenchido
    elif 'human_input' in request.form and request.form['human_input'].strip() != '':
        human_input = request.form['human_input']

    # Se não houver entrada válida, retorna uma mensagem de erro
    if not human_input:
        return "Nenhuma entrada válida foi fornecida."

    # Obtém a resposta da AI
    message = get_response_from_ai(human_input)
    return message

@app.route('/shutdown', methods=['POST'])
def shutdown():
    try:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            return "Não foi possível encerrar o servidor.", 500
        func()
        return "Servidor encerrado."
    except Exception as e:
        print(f"Erro ao tentar encerrar o servidor: {e}", file=sys.stderr)
        return "Erro ao encerrar a sessão.", 500
    finally:
        # Tenta encerrar o navegador
        if browser_process is not None:
            try:
                browser_process.terminate()  # Tenta encerrar o processo do navegador
            except Exception as e:
                print(f"Erro ao tentar encerrar o navegador: {e}", file=sys.stderr)
        
        # Finaliza o processo do Python para garantir o encerramento
        os._exit(0)

def open_browser():
    global browser_process
    # Abre o navegador e obtém a lista de processos antes e depois da abertura
    webbrowser.open("http://127.0.0.1:5000/")
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'chrome' in proc.info['name'].lower() or 'msedge' in proc.info['name'].lower() or 'firefox' in proc.info['name'].lower():
            if "http://127.0.0.1:5000/" in proc.info['cmdline']:
                browser_process = proc
                break

if __name__ == '__main__':
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Controle de abertura única do navegador
    def start_app():
        # Espera um segundo antes de abrir o navegador
        threading.Timer(1, open_browser).start()
        # Executa o servidor Flask
        app.run(use_reloader=False)

    start_app()