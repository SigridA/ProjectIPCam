import sys
sys.path.append('ButtonPressed')
#import ButtonPressed

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	print ("hello")
	return render_template('index.html')
	import ButtonPressed
	
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port=9000, debug=False)
	
