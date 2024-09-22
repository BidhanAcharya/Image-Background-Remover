import streamlit as st
import numpy as np
from io import BytesIO
from PIL import Image
from rembg import remove
import os

st.title("Upload your Image")

# Convert the image to BytesIO so we can download it!
def convert_image(img):
    buffer = BytesIO()  # allows to handle binary data without writing to disk.
    img.save(buffer, format="PNG")  # Saves the image in PNG format to the buffer.
    byte_im = buffer.getvalue()  # Retrieves the byte data from the buffer.
    return byte_im

# Upload the file
image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# If we've uploaded an image, open it and remove the background!
if image_upload:
    image = Image.open(image_upload)  # open the uploaded image file using PIL
    
    # Create two columns
    col1, col2 = st.columns(2)

    # Display the original image in the first column
    with col1:
        st.image(image, caption="Original Image")

    # Remove the background and display the result in the second column
    fixed = remove(image)
    downloadable_image = convert_image(fixed)

    with col2:
        st.image(fixed, caption="Image with Background Removed")

    # Extract original file name without extension
    original_filename = os.path.splitext(image_upload.name)[0]
    download_filename = f"{original_filename} background removed.png"

    # Add a download button for the processed image with the new filename
    st.download_button(
        "Download image", downloadable_image, download_filename, 
    )
