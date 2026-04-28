from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAF9CkZCweGJABRdfotkAjLPnZBOHAPnbpwsAGuet2tiyPmB2I6Ou6lFwZBei6ARurNx0JLR9yJDN0iYMJ10YAXxzlnCBeyvk23nOPIIDLKSn4XH2luvBA0DLQH3a5Rf73KZC0OXc8UhYHJy8CHbDk8NhTt5XPgZBmEHcTVZAZBIbUHY9Cp3GeTtBSauL1PAGpzyrYhiZCMc5tXTXgDdmtQPZB7i9eOcHe3rRjBZArd"
PHONE_NUMBER_ID = "1100816249779252"
VERIFY_TOKEN = "rukshan_whatsapp_bot_2026_secure"

def send_msg(to, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    data = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": text}}
    requests.post(url, headers=headers, json=data)

@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token') == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return 'Error', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]
        send_msg(msg['from'], f"හෙලෝ! ඔයා එව්වේ: {msg['text']['body']}")
    except: pass
    return 'OK', 200

@app.route('/')
def home(): return 'Bot Running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
