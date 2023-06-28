import streamlit as st
import requests

def shorten_url(url, alias=None):
    endpoint = "https://url-shortener23.p.rapidapi.com/shorten"
    payload = {
        "url": url,
        "alias": alias
    }
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "e530f5efc9msh6f2dd7ff7fcc484p189414jsn1d97aae1268a",
        "X-RapidAPI-Host": "url-shortener23.p.rapidapi.com"
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    data = response.json()
    return data.get('short_url')

# Streamlit app
def main():
    st.title("URL Shortener")

    # URL input
    url = st.text_input("Enter the URL to shorten")

    # Alias input (optional)
    alias = st.text_input("Enter an alias (optional)")

    # Shorten button
    if st.button("Shorten"):
        if url:
            short_url = shorten_url(url, alias)
            if short_url:
                st.success(f"Shortened URL: {short_url}")
            else:
                st.error("Failed to shorten URL")
        else:
            st.warning("Please enter a URL to shorten")

if __name__ == "__main__":
    main()
