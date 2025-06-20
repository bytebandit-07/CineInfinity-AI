import requests
from bs4 import BeautifulSoup

def get_image_url(search_term: str) -> str:
    try:
        url = f"https://www.google.com/search?q={search_term}&tbm=isch"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        imgs = soup.find_all("img")
        for img in imgs[1:10]:
            src = img.get("src", "")
            if src.startswith("http"):
                return src
    except Exception as e:
        print("Image scrape error:", e)
    return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"