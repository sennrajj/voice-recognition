from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Inisialisasi pengenalan suara dan engine text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def execute_command(command):
    try:
        if "open file explorer" in command:
            os.system("explorer")  # Membuka File Explorer
            speak("Opening File Explorer")
        elif "open drive c" in command:
            os.system("explorer C:\\")  # Membuka Drive C
            speak("Opening Drive C")
        elif "open drive d" in command:
            os.system("explorer D:\\")  # Membuka Drive D
            speak("Opening Drive D")
        elif "open notepad" in command:
            os.system("start notepad")  # Membuka Notepad
            speak("Opening Notepad")
        elif "open microsoft word" in command:
            os.system(r'"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"')  # Membuka Word
            speak("Opening Microsoft Word")
        elif "open microsoft powerpoint" in command:
            os.system(r'"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"')  # Membuka PowerPoint
            speak("Opening Microsoft Powerpoint")
        elif "open microsoft excel" in command:
            os.system(r'"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"')  # Membuka Excel
            speak("Opening Microsoft Excel")
        elif "open settings" in command:
            os.system("start ms-settings:")  # Membuka Settings
            speak("Opening Settings")
        elif "open downloads" in command:
            os.system("explorer %USERPROFILE%\\Downloads")  # Membuka folder Downloads
            speak("Opening Folder Downloads")
        elif "open documents" in command:
            os.system("explorer %USERPROFILE%\\Documents")  # Membuka folder Documents
            speak("Opening Folder Documents")
        elif "open music" in command:
            os.system("explorer %USERPROFILE%\\Music")  # Membuka folder Music
            speak("Opening Folder Music")
        elif "open pictures" in command:
            os.system("explorer %USERPROFILE%\\Pictures")  # Membuka folder Pictures
            speak("Opening Folder Pictures")
        elif "open videos" in command:
            os.system("explorer %USERPROFILE%\\Videos")  # Membuka folder Videos
            speak("Opening Folder Videos")
        elif "open google chrome" in command:
            os.system("start chrome")  # Membuka Google Chrome
            speak("Opening Google Chrome")
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")  # Membuka YouTube
            speak("Opening YouTube")
        elif "open facebook" in command:
            webbrowser.open("https://www.facebook.com")  # Membuka Facebook
            speak("Opening Facebook")
        elif "open instagram" in command:
            webbrowser.open("https://www.instagram.com")  # Membuka Instagram
            speak("Opening Instagram")
        elif "open github" in command:
            webbrowser.open("https://www.github.com")  # Membuka GitHub
            speak("Opening GitHub")
        elif "exit program" in command:
            speak("Exiting Program, see you again!")
            shutdown_server()
            return "Program exited."  # Mengakhiri program
        else:
            return "Perintah tidak dikenal."
        return f"Perintah '{command}' berhasil dijalankan."
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return "perintah tidak dikenali"
    except sr.RequestError:
        return "tidak dapat menghubungi layanan"
    
def shutdown_server():
    """Fungsi untuk menghentikan server Flask secara paksa."""
    os._exit(0)  # Hentikan server Flask secara langsung
    
# Konfigurasi Email
EMAIL_ADDRESS = 'raj.boygeneration21@gmail.com'
EMAIL_PASSWORD = 'zabc gvax flnp zqkg'  # Gunakan app password jika menggunakan Gmail
RECEIVER_EMAIL = 'rajpresent09@gmail.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/listen', methods=['POST'])
def listen_command():
    command = listen()  # Fungsi mendengarkan suara
    result = execute_command(command)  # Eksekusi perintah
    return jsonify({'command': command, 'result': result})

@app.route('/send-feedback', methods=['POST'])
def send_feedback():
    try:
        # Ambil data dari form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Buat email
        subject = "Feedback dari Pengguna"
        body = f"Nama: {name}\nEmail: {email}\nPesan:\n{message}"
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Kirim email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        return "Feedback berhasil dikirim!", 200

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    speak("Voice Recognition System is now active!")
    app.run(debug=True, port=5006)