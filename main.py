import streamlit as st
from rembg import remove
from PIL import Image
import io

# Page config – wide mode
st.set_page_config(page_title="Background Remover", layout="wide")

# --- Custom Style for 1400px width ---
custom_width_style = """
    <style>
    .appview-container .main .block-container {
        max-width: 1400px;
        padding-left: 2rem;
        padding-right: 2rem;
        margin: auto;
    }
    </style>
"""
st.markdown(custom_width_style, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📤 Upload Image")
    st.markdown("Upload JPG, JPEG, or PNG file to remove background.")
    uploaded_file = st.file_uploader("Choose file", type=["jpg", "jpeg", "png"])
    st.markdown("---")
    st.markdown("👈 Upload from here and see results on the right.")

# Main Content
st.title("🖼️ Background Remover App")
st.markdown("""
This app allows you to **remove background from images** using AI.  
It supports PNG, JPG, and JPEG files.

👉 Steps:
1. Upload an image from the left sidebar  
2. Click the "Remove Background" button  
3. See the original and result side by side  
4. Download the transparent image
""")

# Process Image
if uploaded_file is not None:
    # Read image bytes
    input_bytes = uploaded_file.read()
    input_image = Image.open(io.BytesIO(input_bytes))

    # Show original image
    st.subheader("📷 Original Image")
    st.image(input_image, use_container_width=True)

    if st.button("🚀 Remove Background"):
        with st.spinner("Removing background..."):
            output_bytes = remove(input_bytes)
            output_image = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        st.success("✅ Background removed successfully!")

        # Show result
        st.subheader("🎯 Image with Background Removed")
        st.image(output_image, use_container_width=True)

        # Download
        buf = io.BytesIO()
        output_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 Download Transparent Image",
            data=byte_im,
            file_name="no-background.png",
            mime="image/png"
        )

# --- Custom Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>Made with ❤️ by <b>Bhupendra Singh</b></p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: grey;'>© 2025 Bhupendra Singh | Do not reuse without permission.</p>",
    unsafe_allow_html=True
)

# --- Hide Streamlit default footer/header ---
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
