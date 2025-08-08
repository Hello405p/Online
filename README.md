# GitHub Login Bot

A Python script that automates GitHub login using Selenium WebDriver.

## Features

- 🚀 Automated GitHub login
- 🔍 Comprehensive debugging output
- 🛡️ Multiple fallback strategies for WebDriver setup
- 📝 Detailed logging to both console and file
- 🔧 Robust error handling

## Requirements

- Python 3.7+
- Google Chrome browser
- Internet connection

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv github_bot_env
source github_bot_env/bin/activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Ensure Google Chrome is installed (already done in this environment)

## Usage

### Basic Usage
```bash
python github_login_bot.py
```

### What the bot does:

1. **Navigate to GitHub login page**: `https://github.com/login`
2. **Fill email field**: Enters `dasbristy468@gmail.com`
3. **Fill password field**: Enters `pass`
4. **Click Sign in button**: Submits the login form

## Configuration

You can modify the credentials in the `GitHubLoginBot` class:

```python
self.email = "your_email@gmail.com"
self.password = "your_password"
```

## Debugging

The bot provides extensive debugging information:
- All steps are logged to console
- Detailed logs are saved to `github_bot.log`
- Error messages are captured and displayed
- Page information is displayed before and after login

## Output Example

```
2025-08-08 10:45:39,935 - INFO - 🚀 Starting GitHub login process...
2025-08-08 10:45:41,822 - INFO - ✅ Chrome WebDriver setup successful
2025-08-08 10:45:42,142 - INFO - ✅ Successfully navigated to: https://github.com/login
2025-08-08 10:45:42,239 - INFO - ✅ Email field filled with: dasbristy468@gmail.com
2025-08-08 10:45:42,295 - INFO - ✅ Password field filled
2025-08-08 10:45:42,352 - INFO - ✅ Sign in button clicked
2025-08-08 10:45:45,362 - INFO - ✅ Login appears successful - redirected away from login page
```

## Browser Configuration

The bot runs in headless mode by default for better performance in server environments. To see the browser in action, comment out the headless option in the `setup_driver` method:

```python
# chrome_options.add_argument("--headless")
```

## Files

- `github_login_bot.py` - Main bot script
- `requirements.txt` - Python dependencies
- `github_bot.log` - Detailed log file (created when bot runs)
- `README.md` - This documentation

## Troubleshooting

1. **ChromeDriver issues**: The bot automatically downloads the correct ChromeDriver version
2. **Chrome not found**: Ensure Google Chrome is installed at `/usr/bin/google-chrome-stable`
3. **Permission errors**: Make sure you have proper permissions to run the script

## Security Note

⚠️ **Important**: This bot is for educational/testing purposes. Never commit real passwords to version control. Consider using environment variables for sensitive credentials in production scenarios.

## License

This project is for educational purposes only.