from flask import Flask, render_template, current_app as app

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    @app.route('/')
    def index():
        return
















    
