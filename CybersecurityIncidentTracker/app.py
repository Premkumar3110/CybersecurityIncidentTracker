from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
incidents = []

@app.route('/')
def index():
    return render_template('index.html', incidents=incidents)

@app.route('/report', methods=['POST'])
def report():
    incident = request.form['incident']
    incidents.append(incident)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)