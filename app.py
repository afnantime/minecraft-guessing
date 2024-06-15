import json
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load blocks from blocks.json
with open('static/blocks.json', 'r') as f:
    blocks = json.load(f)

@app.route('/')
def index():
    # Load blocks from blocks.json
    with open('static/blocks.json', 'r') as f:
        blocks_data = json.load(f)
    
    # Randomly select a block
    selected_block = random.choice(blocks_data)
    initial_hint = random.choice(selected_block['hints'])
    total_hints = len(selected_block['hints'])
    
    # Pass the block name, initial hint, and total hints to the HTML template
    return render_template('index.html', initial_hint=initial_hint, block_name=selected_block['name'], total_hints=total_hints)

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess = data.get('guess')
    block_name = data.get('block_name')
    if guess.lower() == block_name.lower():
        message = "Correct guess!"
        success = True
    else:
        message = "Incorrect guess. Try again!"
        success = False
    return jsonify({'success': success, 'message': message})

@app.route('/get_hint', methods=['POST'])
def get_hint():
    data = request.json
    block_name = data.get('block_name')
    used_hints = data.get('used_hints')
    
    block = next((block for block in blocks if block['name'] == block_name), None)
    if block:
        available_hints = [hint for hint in block['hints'] if hint not in used_hints]
        if available_hints:
            return jsonify({'hint': random.choice(available_hints)})
    
    return jsonify({'hint': None})

if __name__ == '__main__':
    app.run(debug=True)