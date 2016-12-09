from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    localtime = time.asctime( time.localtime(time.time()) )
    return localtime

@app.route('/hora')
def seg():
    #return render_template('segons.html',segons=time.strftime("%S"))
    return (time.strftime("%S")) 
    #return (time.strftime("%H:%M:%S"))
	
@app.route('/activate')
def activate():
	fo = open("foo.txt", "w")
	text = request.args.get('text')
	fo.write(text)
	fo.close()
	return "OK"

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )