from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Tssukenberg ver. 0.1"