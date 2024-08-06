# telegram_api_search_bot

This project is a Telegram bot built using the Telethon library. The bot allows users to search for Telegram groups by keyword, group name or topic. It interacts with a FastAPI server to retrieve and display the search results.

# Features

- `/start` Command: Greets the user and provides usage instructions.
- `/search` Command: Allows users to search for Telegram groups by providing a keyword.

# Installation and Setup

Prerequisites:

- A Telegram account
- API ID and API Hash from Telegram
- A Telegram bot token

# Environment Variables

Create a `.env` file in the root directory and set the following variables:

- `API_ID`=<your_api_id>
- `API_HASH`=<your_api_hash>
- `BOT_TOKEN`=<your_bot_token>

**Note:** Ensure your `.env` file is listed in `.gitignore` to prevent sensitive information from being uploaded to version control systems.

# Installation


**Install Dependencies:**

```shell
pip install -r requirements.txt
```

**Run the FastAPI Server:**

Ensure your [FastAPI server](https://github.com/hasanMasalha/telegram_api_search_server) is running and accessible. Follow the instructions in the `README.md` file that is provided in the server repository. 

**Start the Bot:**

```shell
python bot.py
```

# Usage

- `/start`: Initiates interaction with the bot and provides instructions.
- `/search <keyword>`: Searches for groups based on the provided keyword. The bot will display a list of matching groups.

# Troubleshooting

- Ensure your `.env` file is correctly set up with the API credentials.
- Verify that the FastAPI server is running and accessible.
