# Instagram Profile Image Downloader

This Python script allows you to download the profile image of any Instagram user by providing their username. It utilizes web scraping techniques with BeautifulSoup and urllib to extract the profile image URL from the user's Instagram profile page.

## Prerequisites

Before running the script, ensure you have Python installed on your system. If not, you can download and install it from the official Python website: [python.org](https://www.python.org/).

Additionally, make sure to have the `beautifulsoup4` library installed. You can install it via pip:

```bash
pip install beautifulsoup4
```
## Usage
Run the Script:

Execute the script by running the following command in your terminal or command prompt:

```bash
python download_profile_image.py
```
Enter Username:

You'll be prompted to enter the username of the Instagram account whose profile image you want to download. Provide the exact username without any extra characters or spaces.

Download Profile Image:

Once you've provided the username, the script will attempt to access the user's Instagram profile page and extract the URL of their profile image. If successful, it will download the image and save it locally with the format {username}_profile_pic.jpg.

Check Output:

After execution, check the directory where the script is located to find the downloaded profile image with the username as part of the filename.

Example
Let's say you want to download the profile image of the Instagram user with the username example_user. Here's how you would use the script:

plaintext
Copy code
Enter the username: example_user
After providing the username, the script will fetch the profile image and save it locally. You will see a confirmation message indicating that the profile image has been downloaded successfully.

Error Handling
The script includes error handling to manage situations where it is unable to access the user's profile page or retrieve the profile image URL. If any errors occur during the process, appropriate error messages will be displayed in the console to inform you about the issue.
