### G4F Chatbot using Flask

![Screenshot](screenshot.png)

This repository contains a Flask application that integrates the G4F chatbot using OpenAI's GPT-3.5 model. The chatbot allows users to interact via a web interface.

### Setup

1. **Installation**

   Ensure you have Python and pip installed. Clone the repository and navigate into the directory:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

   Install the required Python packages:

   ```bash
   pip install Flask openai
   ```

2. **Configuration**

   Obtain your OpenAI API key and set it as an environment variable:

   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

   Replace `'your-api-key'` with your actual OpenAI API key.

3. **Running the Application**

   Start the Flask development server:

   ```bash
   python app.py
   ```

   The application will run on `http://localhost:5000`.

### Usage

- Access the application by navigating to `http://localhost:5000` in your web browser.
- Enter a message in the chatbox and press Enter or Send to receive a response from the G4F chatbot.

### Files and Directory Structure

- `app.py`: Contains the Flask application code.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static files (e.g., CSS, JavaScript).
- `README.md`: This file documenting the project.

### Screenshots

![Screenshot](screenshot.png)

### Credits

- Developed by Anubhav Chaturvedi.
- Powered by OpenAI's GPT-3.5 model.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
