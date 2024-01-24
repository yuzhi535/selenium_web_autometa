import streamlit as st
from extract import take_webdata
from PIL import Image
from io import BytesIO

def main():
    st.title("Website Content Exctractor")
    
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
            html_image, html_content = take_webdata(url)
            st.subheader("Website title:")
            if html_content:
                st.info(html_content)
            else:
                st.error("Error: empty html content")
            st.subheader("Website preview:")
            if html_image:
                st.image(html_image)
            else:
                st.error("Error: empty html preview")
                                   
    
    except Exception as e:
        st.error(f"Error: {e}")



if __name__ == "__main__":
    main()
