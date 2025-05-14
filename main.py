from flask import Flask, render_templete, request
import os

# Define a pasta onde estão os arquivos HTML
# (neste caso, a nariz do projeto)
templete_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=templete_dir)

# Direcionamento para base do index HTML
@app.route("/") 
def home ():
     return render_templete("index.html")

if __name__ == "__main__":
     app.run(host= "0.0.0.0", port=3000)