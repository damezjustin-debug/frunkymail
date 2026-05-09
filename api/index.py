from flask import Flask, request, jsonify

app = Flask(__name__)

# Tambahin route buat ngetes di browser (Home)
@app.route('/')
def home():
    return "Server FrunkyMail Aktif, Kirim POST ke /email-handler."

# Route buat nerima email
@app.route('/email-handler', methods=['GET', 'POST']) # Tambahin GET biar bisa dibuka browser
def handle_email():
    if request.method == 'POST':
        data = request.json or {}
        sender = data.get('from', 'Unknown')
        subject = data.get('subject', 'No Subject')
        print(f"Email masuk: {subject}")
        return jsonify({"status": "Email received!"}), 200
    
    # Kalau dibuka lewat browser (GET) munculin ini
    return jsonify({"message": "Gunakan POST buat kirim data email"}), 200

# Entry point buat Vercel
def handler(event, context):
    return app(event, context)
