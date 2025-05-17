from flask import Flask, request, jsonify, render_template, redirect
from datetime import datetime
import json, os

app = Flask(__name__)

JSON_NOTES_FILE = 'data/notes.json'
MD_NOTES_FILE = 'data/notes.md'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

def read_notes():
    if not os.path.exists(JSON_NOTES_FILE):
        return []
    with open(JSON_NOTES_FILE, 'r') as f:
        return json.load(f)

def write_notes(notes):
    with open(JSON_NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

def append_to_markdown(note_text):
    today = datetime.now().strftime('%Y-%m-%d')
    entry_header = f"# Notes - {today}\n"
    entry = f"- {note_text}\n"

    if os.path.exists(MD_NOTES_FILE):
        with open(MD_NOTES_FILE, 'r+') as f:
            content = f.read()
            if entry_header not in content:
                f.write(f"\n{entry_header}{entry}")
            else:
                f.write(entry)
    else:
        with open(MD_NOTES_FILE, 'w') as f:
            f.write(f"{entry_header}{entry}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note', '').strip()
        if note:
            # Save to JSON
            notes = read_notes()
            note_entry = {
                "text": note,
                "timestamp": datetime.now().isoformat()
            }
            notes.append(note_entry)
            write_notes(notes)

            # Save to Markdown
            append_to_markdown(note)

        return redirect('/')
    
    return render_template('index.html')

@app.route('/api/notes', methods=['GET', 'POST'])
def api_notes():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '').strip()
        if text:
            notes = read_notes()
            note_entry = {
                "text": text,
                "timestamp": datetime.now().isoformat()
            }
            notes.append(note_entry)
            write_notes(notes)

            append_to_markdown(text)

            return jsonify({"message": "Note added"}), 201
        return jsonify({"error": "Note text required"}), 400

    return jsonify(read_notes())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
