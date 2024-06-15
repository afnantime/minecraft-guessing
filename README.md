# Minecraft Guessing Game

This project is a web-based guessing game where players try to guess the name of a Minecraft block based on hints provided. The game is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- Randomly selects a Minecraft block and provides an initial hint.
- Allows users to guess the block name.
- Provides additional hints upon request.
- Displays a dropdown of block names for easier guessing.

## Setup

1. **Clone the repository:**
   ```sh
   https://github.com/afnantime/minecraft-guessing.git
   cd minecraft-guessing-game
   ```

2. **Install dependencies:**
   ```sh
   pip install flask
   ```

3. **Run the application:**
   ```sh
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

## File Structure

- `app.py`: Main Flask application.
- `static/blocks.json`: JSON file containing block data and hints.
- `templates/index.html`: HTML template for the game interface.
- `static/img/`: Directory containing images of Minecraft blocks.

## API Endpoints

- **`GET /`**: Renders the main game page.
- **`POST /guess`**: Checks the user's guess.
- **`POST /get_hint`**: Provides an additional hint.

## Example JSON Structure (`blocks.json`)

```json
[
  {
    "name": "Redstone Block",
    "image": "static/img/Block_of_Redstone.webp",
    "hints": [
      "A block that pulses with energy, powering contraptions far and wide.",
      "The lifeblood of machinery and automation, glowing with potential."
    ]
  },
  ...
]
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

---
