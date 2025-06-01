import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO


def search_and_show_image():
    searchTerm = input("Enter search term: ")

    def get_image_url(searchTerm):
        try:
            searchUrl = f"https://www.google.com/search?q={searchTerm}&tbm=isch"
            headers = {
                "User-Agent": "Mozilla/5.0"
            }
            response = requests.get(searchUrl, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')

            for img in img_tags[1:10]:  # Skip first one (Google logo)
                if img.has_attr('src') and img['src'].startswith('http'):
                    return img['src']
            return 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
        except Exception as e:
            print("Error fetching image URL:", e)
            return 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'

    def show_image(image_url):
        try:
            response = requests.get(image_url)
            image_data = Image.open(BytesIO(response.content))
            max_size = (600, 600)
            image_data.thumbnail(max_size, Image.LANCZOS)

            root = Tk()
            root.title("Image Viewer")
            img = ImageTk.PhotoImage(image_data)
            panel = Label(root, image=img)
            panel.pack()
            root.mainloop()
        except Exception as e:
            print("Error displaying image:", e)

    url = get_image_url(searchTerm)
    print("Image URL:", url)
    show_image(url)


# Call the function
search_and_show_image()