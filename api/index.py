from flask import Flask, request, jsonify

app = Flask(__name__)

# Ini buat ngetes di browser: https://frunkymail.vercel.app/
@app.route('/')
def hello():
    return "<h1>FrunkyMail is Online!</h1><p>Kirim POST ke /api/index buat email.</p>"

# Ini buat nerima data email dari Cloudflare
@app.route('/api/index', methods=['POST', 'GET'])
def email_receiver():
    if request.method == 'POST':
        data = request.json
        return jsonify({"status": "diterima", "data": data}), 200
    return jsonify({"status": "ready", "note": "Gunakan POST buat kirim email"}), 200

# Vercel butuh ini buat ngenalin Flask-nya
app = app
