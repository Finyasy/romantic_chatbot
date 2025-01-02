# 💖 Romantic Chatbot

Welcome to the **Romantic Chatbot** project! This chatbot leverages OpenAI's GPT-4o-mini model to generate heartwarming, romantic responses based on user input. Perfect for anyone looking to add a little charm to their conversations. ✨

---

## 🚀 Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7+
- `python-dotenv` package
- OpenAI API key

---

### 🛠️ Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/romantic_chatbot.git
   cd romantic_chatbot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   - In the root directory, create a `.env` file and add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Add `.env` to `.gitignore`**:
   - Ensure the `.env` file is not pushed to GitHub by adding it to your `.gitignore` file:
     ```plaintext
     .env
     ```

6. **Remove `.env` from Git Tracking** (if already tracked):
   ```bash
   git rm --cached .env
   ```

7. **Commit the Changes**:
   ```bash
   git add .gitignore
   git commit -m "Add .env to .gitignore and remove it from tracking"
   ```

8. **Push the Changes to GitHub**:
   ```bash
   git push origin main
   ```

---

## 💬 Usage

1. **Run the Chatbot**:
   ```bash
   python chat_handler.py
   ```

2. **Interact with the Chatbot**:
   - The chatbot will prompt you for input and generate romantic responses based on your input. ❤️

3. **Access the Bot on Telegram**:
   - Once deployed to Heroku, you can find your bot at [t.me/WincyBot](https://t.me/WincyBot). 
   - Add a description, an about section, and a profile picture to personalize your bot.
   - For more commands, see `/help` in Telegram. If you want a better username for your bot, contact Bot Support once it is fully operational.

---

## 🌐 Deployment to Heroku

Follow these steps to deploy your chatbot to Heroku:

1. **Login to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a Heroku App**:
   ```bash
   heroku create your-app-name
   ```

3. **Add Buildpacks**:
   - Set up Python and Node.js buildpacks for your app:
     ```bash
     heroku buildpacks:add heroku/python
     heroku buildpacks:add heroku/nodejs
     ```

4. **Push the Code to Heroku**:
   ```bash
   git push heroku main
   ```

5. **Set Environment Variables**:
   - Add your OpenAI API key as a config variable:
     ```bash
     heroku config:set OPENAI_API_KEY=your_openai_api_key
     ```

6. **Scale the App**:
   - Ensure at least one dyno is running:
     ```bash
     heroku ps:scale web=1
     ```

7. **Access Your Bot**:
   - Your bot is now live and accessible via Telegram at [t.me/WincyBot](https://t.me/WincyBot).

---

## 📂 Code Overview

### `chat_handler.py`

#### **Imports**:
- `asyncio`, `os`, `dotenv`, `OpenAI`

#### **Environment Variables**:
- Loads the OpenAI API key from the `.env` file.

#### **Client Initialization**:
- Initializes the OpenAI client with the API key.

#### **Chat History**:
- Maintains a list of chat history to provide context for responses.

#### **`romantic_chat` Function**:
- Asynchronously generates a romantic response based on user input.

#### **`handle_message` Function**:
- Handles incoming messages and generates responses using the `romantic_chat` function.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

### 🖋️ Notes

- Replace `your_openai_api_key` with your actual OpenAI API key.
- Replace `your-username` with your GitHub username.

Once ready, save and commit this file to your repository:

```bash
git add README.md
git commit -m "Add project documentation"
git push origin main
```

Enjoy building your romantic chatbot! 🌹

