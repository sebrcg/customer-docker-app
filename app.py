from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = "v6.0"
    weclome_msg = os.getenv('WELCOME_MESSAGE', 'Welcome!')
    return f'''
      <h1>Custom Docker App {version}</h1>
      <p>🎉 {welcome_msg}</p>
      <p>Full DevOps Pipeline Demo! 🚀</p>
      <p>CI/CD → GitOps → Encrypted Secrets → Ingress</p>
      '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'version'; 'v6.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

