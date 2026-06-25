import requests
import streamlit as st
st.write("Hello StreamLit. This is Sudha, testing the app on 25th June, Thursday")
from pypdf import PdfReader
import base64

st.set_page_config(page_title="Local PDF Viewer", layout="wide")
st.title("📄 Local PDF Browser & Viewer")

# 1. File Uploader widget to browse local drive
uploaded_file = st.file_uploader("Choose a PDF file from your local drive", type=["pdf"])

if uploaded_file is not None:
    # Create two columns for a side-by-side view
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Visual PDF Display")
        
        # Read file as bytes for embedding
        bytes_data = uploaded_file.read()
        
        # Convert PDF to Base64 to embed it in an HTML iframe
        base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
        
        # Render the iframe
        st.markdown(pdf_display, unsafe_allow_html=True)

    with col2:
        st.subheader("Extracted Text Content")
        
        # Reset file pointer after reading for the iframe
        uploaded_file.seek(0)
        
        # Load PDF using pypdf
        reader = PdfReader(uploaded_file)
        num_pages = len(reader.pages)
        
        # Let user select which page's text to view
        page_num = st.number_input(f"Select Page (1 to {num_pages})", min_value=1, max_value=num_pages, value=1)
        
        # Extract and display the text
        page = reader.pages[page_num - 1]
        text = page.extract_text()  
        
        if text.strip():
            st.text_area(f"Text from Page {page_num}:", text, height=600)
        else:
            st.warning("No extractable text found on this page (it might be a scanned image).")
            
else:
    st.info("Please upload a PDF file to view its content.")
