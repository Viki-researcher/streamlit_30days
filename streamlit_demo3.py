import streamlit as st
import requests
import json
import urllib.parse
from PIL import Image
from io import BytesIO

def main():
    st.title("Pixabay Image Viewer")
    
    # Add UI elements and functionality here
    keyword = st.text_input("Enter a keyword:")
    num_images = st.slider("Select the number of images:", 1, 10, 3)
    if st.button("Fetch and Display Images"):
        fetch_and_display_images(keyword, num_images)


def fetch_and_display_images(keyword, num_images):
    encoded_keyword = urllib.parse.quote(keyword)
    api_url = f"https://pixabay.com/api/?key={'38268462-c86823f2fc842d4845dabd4bc'}&q={encoded_keyword}&per_page={num_images}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    for hit in data['hits']:
        image_url = hit['webformatURL']
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        st.image(img)

if __name__ == "__main__":
    main()