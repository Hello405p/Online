#!/usr/bin/env python3
"""
GitHub Login Bot
Automates login to GitHub using Selenium WebDriver
Author: AI Assistant
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging for debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/workspace/github_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GitHubLoginBot:
    def __init__(self):
        """Initialize the GitHub login bot"""
        self.driver = None
        self.email = "dasbristy468@gmail.com"
        self.password = "pass"
        self.login_url = "https://github.com/login"
        
    def setup_driver(self):
        """Set up Chrome WebDriver with options"""
        logger.info("Setting up Chrome WebDriver...")
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")
        chrome_options.add_argument("--remote-debugging-port=9222")
        
        # Set the path to Chrome browser
        chrome_options.binary_location = "/usr/bin/google-chrome-stable"
        
        # Run in headless mode for Linux environment
        chrome_options.add_argument("--headless")
        
        try:
            # Use webdriver-manager to automatically download and manage ChromeDriver
            # Specify the Chrome version to match Chromium
            service = Service(ChromeDriverManager(driver_version="120.0.6099.109").install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.implicitly_wait(10)
            logger.info("✅ Chrome WebDriver setup successful")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to setup Chrome WebDriver with webdriver-manager: {e}")
            logger.info("Trying with system ChromeDriver...")
            
            # Fallback to system chromedriver if available
            try:
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.implicitly_wait(10)
                logger.info("✅ Chrome WebDriver setup successful with system driver")
                return True
            except Exception as e2:
                logger.error(f"❌ Failed to setup Chrome WebDriver with system driver: {e2}")
                return False
    
    def navigate_to_login(self):
        """Navigate to GitHub login page"""
        logger.info(f"Navigating to GitHub login page: {self.login_url}")
        
        try:
            self.driver.get(self.login_url)
            logger.info(f"✅ Successfully navigated to: {self.driver.current_url}")
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            logger.info("✅ Page loaded successfully")
            return True
            
        except TimeoutException:
            logger.error("❌ Timeout waiting for page to load")
            return False
        except Exception as e:
            logger.error(f"❌ Error navigating to login page: {e}")
            return False
    
    def fill_email_field(self):
        """Fill the email/username field"""
        logger.info("Looking for email/username field...")
        
        try:
            # Try multiple selectors for the email field
            email_selectors = [
                "#login_field",
                "input[name='login']",
                "input[type='text']",
                "input[autocomplete='username']"
            ]
            
            email_field = None
            for selector in email_selectors:
                try:
                    email_field = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    logger.info(f"✅ Found email field using selector: {selector}")
                    break
                except TimeoutException:
                    continue
            
            if not email_field:
                raise NoSuchElementException("Email field not found with any selector")
            
            # Clear and fill email field
            email_field.clear()
            email_field.send_keys(self.email)
            logger.info(f"✅ Email field filled with: {self.email}")
            
            # Verify the field was filled
            if email_field.get_attribute("value") == self.email:
                logger.info("✅ Email field value verified")
                return True
            else:
                logger.warning("⚠️ Email field value verification failed")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error filling email field: {e}")
            return False
    
    def fill_password_field(self):
        """Fill the password field"""
        logger.info("Looking for password field...")
        
        try:
            # Try multiple selectors for the password field
            password_selectors = [
                "#password",
                "input[name='password']",
                "input[type='password']",
                "input[autocomplete='current-password']"
            ]
            
            password_field = None
            for selector in password_selectors:
                try:
                    password_field = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    logger.info(f"✅ Found password field using selector: {selector}")
                    break
                except TimeoutException:
                    continue
            
            if not password_field:
                raise NoSuchElementException("Password field not found with any selector")
            
            # Clear and fill password field
            password_field.clear()
            password_field.send_keys(self.password)
            logger.info("✅ Password field filled")
            
            # Verify the field was filled (check length since password value is hidden)
            if len(password_field.get_attribute("value")) == len(self.password):
                logger.info("✅ Password field value verified")
                return True
            else:
                logger.warning("⚠️ Password field value verification failed")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error filling password field: {e}")
            return False
    
    def click_sign_in_button(self):
        """Click the Sign in button"""
        logger.info("Looking for Sign in button...")
        
        try:
            # Try multiple selectors for the sign in button
            signin_selectors = [
                "input[type='submit'][value='Sign in']",
                "button[type='submit']",
                "input[value='Sign in']",
                ".btn-primary",
                "[data-signin-label]"
            ]
            
            signin_button = None
            for selector in signin_selectors:
                try:
                    signin_button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    logger.info(f"✅ Found Sign in button using selector: {selector}")
                    break
                except TimeoutException:
                    continue
            
            if not signin_button:
                raise NoSuchElementException("Sign in button not found with any selector")
            
            # Click the sign in button
            signin_button.click()
            logger.info("✅ Sign in button clicked")
            
            # Wait a moment to see the result
            time.sleep(3)
            
            # Check if login was successful by looking at URL change
            current_url = self.driver.current_url
            logger.info(f"Current URL after login attempt: {current_url}")
            
            if "github.com/login" not in current_url:
                logger.info("✅ Login appears successful - redirected away from login page")
                return True
            else:
                logger.warning("⚠️ Still on login page - login may have failed")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error clicking sign in button: {e}")
            return False
    
    def debug_page_info(self):
        """Print debug information about the current page"""
        logger.info("=== DEBUG PAGE INFO ===")
        logger.info(f"Current URL: {self.driver.current_url}")
        logger.info(f"Page Title: {self.driver.title}")
        
        # Check for any error messages
        try:
            error_elements = self.driver.find_elements(By.CSS_SELECTOR, ".flash-error, .error, .alert-danger")
            if error_elements:
                for error in error_elements:
                    if error.is_displayed():
                        logger.warning(f"Error message found: {error.text}")
            else:
                logger.info("No error messages found")
        except Exception:
            pass
        
        logger.info("=== END DEBUG INFO ===")
    
    def login(self):
        """Main login process"""
        logger.info("🚀 Starting GitHub login process...")
        
        try:
            # Setup driver
            if not self.setup_driver():
                return False
            
            # Navigate to login page
            if not self.navigate_to_login():
                return False
            
            self.debug_page_info()
            
            # Fill email field
            if not self.fill_email_field():
                return False
            
            # Fill password field
            if not self.fill_password_field():
                return False
            
            # Click sign in button
            if not self.click_sign_in_button():
                return False
            
            self.debug_page_info()
            
            logger.info("🎉 Login process completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Unexpected error during login: {e}")
            return False
        
        finally:
            # Keep browser open for a few seconds to see the result
            logger.info("Keeping browser open for 5 seconds...")
            time.sleep(5)
    
    def close(self):
        """Close the browser"""
        if self.driver:
            logger.info("Closing browser...")
            self.driver.quit()
            logger.info("✅ Browser closed")

def main():
    """Main function to run the GitHub login bot"""
    bot = GitHubLoginBot()
    
    try:
        success = bot.login()
        if success:
            print("\n🎉 GitHub login bot completed successfully!")
        else:
            print("\n❌ GitHub login bot failed. Check the logs for details.")
            
    except KeyboardInterrupt:
        logger.info("Bot interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()