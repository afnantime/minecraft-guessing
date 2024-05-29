import json
import random
from fuzzywuzzy import fuzz
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load blocks from blocks.json
with open('static/blocks.json', 'r') as f:
    blocks = json.load(f)

# Function to check the guess
def check_guess(guess, block_name, threshold):
    # Implement your fuzzy matching logic here
    return guess.lower() == block_name.lower()  # Placeholder logic, adjust as needed

@app.route('/')
def index():
    # Load blocks from blocks.json
    with open('static/blocks.json', 'r') as f:
        blocks_data = json.load(f)
    
    # Randomly select a block
    selected_block = random.choice(blocks_data)
    initial_hint = random.choice(selected_block['hints'])
    
    # Pass the block name and initial hint to the HTML template
    return render_template('index.html', initial_hint=initial_hint, block_name=selected_block['name'])

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess = data.get('guess')
    block_name = data.get('block_name')
    threshold = 80  # Set your fuzzy matching threshold here
    if check_guess(guess, block_name, threshold):
        message = "Correct guess!"
        success = True
    else:
        message = "Incorrect guess. Try again!"
        success = False
    return jsonify({'success': success, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)