from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/email-handler', methods=['POST'])
def handle_email():
    # Cloudflare bakal kirim data via POST request
    data = request.json
    
    sender = data.get('from', 'Unknown')
    subject = data.get('subject', 'No Subject')
    content = data.get('text', 'Empty')

    # Di sini lu bebas mau ngapain, misal print doang dulu
    print(f"Email masuk dari {sender}: {subject}")

    # Balikin respon sukses ke Cloudflare
    return jsonify({"status": "Email received, Bro!"}), 200

# Penting buat Vercel
def handler(event, context):
    return app(event, context)
