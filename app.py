from flask import Flask, request, jsonify, render_template
import json, os

app = Flask(__name__)
NOTES_FILE = 'data/notes.json'

def read_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        return json.load(f)

def write_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        data = request.get_json()
        notes = read_notes()
        notes.append(data)
        write_notes(notes)
        return jsonify({"message": "Note added"}), 201
    return jsonify(read_notes())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
