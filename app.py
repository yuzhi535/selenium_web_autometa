import streamlit as st
from extract import take_screenshot
from PIL import Image
from io import BytesIO

def main():
    st.title("Website Visualizer")
    
    # Get website URL from user input
    url = st.text_input("Enter a URL:", "")
    if st.button("Proceed"):
        if not url:
            st.warning("URL is empty.")
        else:
            visualize(url)
  

def visualize(url):  
    try:
    # Fetch and display the website content
        with st.spinner("loading website data ..."):
            # innerHTML = get_innerHTML(url)
            innerHTML = take_screenshot(url)
            st.subheader("Website preview:")
            if innerHTML:
                st.Image(innerHTML)
            else:
                st.error("Error: empty html")
    
    except Exception as e:
        st.error(f"Error: {e}")



if __name__ == "__main__":
    main()
