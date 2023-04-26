import urllib.request
from bs4 import BeautifulSoup

def download_profile_image(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        html = urllib.request.urlopen(url)
    except:
        print(f"Unable to access {username}'s profile.")
        return
    soup = BeautifulSoup(html, "html.parser")
    img_url = soup.find("meta", property="og:image")["content"]
    img_data = urllib.request.urlopen(img_url).read()
    with open(f"{username}_profile_pic.jpg", "wb") as f:
        f.write(img_data)
    print(f"Profile image for {username} downloaded successfully.")

if __name__ == "__main__":
    
    username = input("Enter the username: ")
    download_profile_image(username)
