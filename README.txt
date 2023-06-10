# LinkedIn Automation Script

This is a Python script that utilizes Selenium WebDriver to automate certain actions on LinkedIn. It allows you to log in, perform searches, and connect with LinkedIn users based on the search results.

## Author

- [Priyanshu](https://github.com/thor149)

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (compatible with your Chrome browser version)

## Setup

1. Clone the repository or download the script file.
2. Install the required dependencies using pip:
3. Download the appropriate Chrome WebDriver executable and place it in the same directory as the script. Make sure it matches your Chrome browser version.

## Usage

1. Open the script file and modify the following placeholders:
- `YOUR-EMAIL-ID`: Replace with your LinkedIn email address.
- `YOUR-PASSWORD`: Replace with your LinkedIn password.
- `-KEYWORD-`: Replace with the keyword you want to search on LinkedIn.
2. Save the changes to the script file.
3. Run the script using the following command:
4. The script will open a Chrome browser, log in to LinkedIn, perform the search, and start connecting with LinkedIn users based on the search results. You can specify the number of connections to make by modifying the `count` parameter in the `connect` function.
5. Once the script finishes, it will print the number of successfully connected people and the remaining connections.

## Notes

- The script includes necessary waiting periods to ensure the page loads properly and elements are visible before interacting with them.
- In case an `ElementClickInterceptedException` occurs, the script will click the next available "Connect" button instead.
- Make sure to use the script responsibly and respect LinkedIn's terms of service.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

