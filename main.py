from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = ['hi','hell']

@app.route('/')
def home():
    return render_template('index.html', notes= notes)

@app.route('/submitNote', methods= ['POST', 'GET'])
def submitNote():
    print(request.form, request.form['noteText'])
    notes.append(request.form['noteText'])
    return redirect('/')

@app.route('/remove/<note>')
def removeNote(note):
    notes.remove(note)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)