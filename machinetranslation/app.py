from flask import Flask, render_template
from package_folder_structure import translator
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/englishToFrench/<text>', methods=['POST','GET'])
def englishToFrench(text):
    en_fr = translator.Trans_English_To_French(text)
    return en_fr.convert_EN_FR()

@app.route('/frenchToEnglish/<text>', methods=['POST','GET'])
def frenchToEnglish(text):
    fr_en = translator.Trans_French_To_English(text)
    return fr_en.convert_FR_EN()




if __name__ == "__main__":
    app.run(debug=True)