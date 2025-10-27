from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Custom Docker App v4.0!</h1><p>Multi-Environment Deployment! 🌍</p>'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

