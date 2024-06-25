# TikTok Shop Singer Tap

This project is a Singer tap application that extracts data from the TikTok Shop API. It uses Poetry for dependency management and includes an OAuth flow to obtain an access token.

## Requirements

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- TikTok Developer account with an approved application

## Setup

### 1. Clone the Repository

bash:
git clone https://github.com/yourusername/official-website-template.git
cd official-website-template

### 2. Install Dependencies
Use Poetry to install the required dependencies:

bash:
poetry install

### 3. Configure Your Application
Create a sample_config.json file in the root directory and fill it with your own API key, secret, and access token. You can use the following template:

json:
{
  "app_key": "your_app_key",
  "app_secret": "your_app_secret",
  "access_token": "your_access_token",
  "start_date": "2020-01-01"
}

### 4. Obtain Access Token
If you don't have an access token yet, follow these steps:

## 1. Run the OAuth flow to get the access token:

poetry run python tiktok_tap/auth.py

## 2.Authorize the App:

Open a web browser and navigate to http://localhost:5000/.
Log in to your TikTok account and authorize the application.

## 3. Retrieve the Access Token:

After authorizing the app, TikTok will redirect you back to http://localhost:5000/callback and display the access token.

## 4. Update sample_config.json:

Replace "your_access_token" in sample_config.json with the obtained access token.