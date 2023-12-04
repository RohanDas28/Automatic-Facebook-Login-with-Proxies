
# Automatic Facebook Login with NodeMaven Proxy

Let’s get into the automation of Facebook login using SeleniumWire for request manipulation and NodeMaven's Residential Proxies to ensure a seamless and secure connection. By the end of this guide, you'll have a script that effortlessly logs into Facebook, benefiting from the enhanced privacy and diverse IP addresses provided by NodeMaven.

## Setting Up SeleniumWire and ChromeDriver:

Begin by installing the necessary Python libraries:

    pip install selenium-wire
    
    pip install webdriver_manager

Now, let's configure the script with the required imports and set up a SeleniumWire-enabled ChromeDriver:

    from seleniumwire import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    import users
    import time

## Proxy Configuration with NodeMaven:
NodeMaven's Residential Proxies offer a reliable solution for web scraping tasks. Integrate them into your script using the provided code:

    # Proxy configuration_
    proxy_username =  'username'
    proxy_password =  'password'
    proxy_url =  f'http://{proxy_username}:{proxy_password}@gate.nodemaven.com:8080'
    seleniumwire_options = {'proxy': {'http': proxy_url, 'verify_ssl': True}}

## Automating Facebook Login:

Initialize the WebDriver and navigate to Facebook:

    # WebDriver setup
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)
    
    # Navigate to Facebook
    driver.get("https://www.facebook.com")

Make sure that your users.py file is structured like this:

    # users.py
    username = "your_facebook_username"
    password = "your_facebook_password"
This way, your script remains clean, and sensitive information such as usernames and passwords are stored in a separate file for better security and organization.
Locate the login elements and input your credentials for automation:

    # Find login elements
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
    login_btn = driver.find_element(By.NAME, "login")
    
    # Input login credentials and click login
    email_input.send_keys(users.username)
    password_input.send_keys(users.password)
    login_btn.click()
## Wait and Cleanup:
To ensure a successful login, incorporate a sleep timer. Finally, close the browser window when the task is complete:

    # Wait for 60 seconds (replace with appropriate wait conditions)
    time.sleep(60)
    
    # Close the browser window when done
    driver.quit()

## NodeMaven's Residential Proxies – Simplifying Automation:

NodeMaven's Residential Proxies play a crucial role in simplifying and securing the automation process. To get started, register on the NodeMaven platform using [this link](https://go.nodemaven.com/proxies1), choose the trial on your personal account, and apply the coupon code 500FREE during the trial setup to receive 500MB of traffic for free.

## Conclusion:

By automating Facebook login with SeleniumWire and integrating NodeMaven's Residential Proxies, you can streamline your processes, ensuring privacy, security, and efficient handling of diverse IP addresses. Follow the steps outlined in this guide to create a robust script that automates Facebook login seamlessly. Happy automating!
