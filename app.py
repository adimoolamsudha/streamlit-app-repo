import streamlit as st
import fitz
st.title("PDF Extractor")

def fn_reset_form():
  st.session_state.pop("uploaded_file",None)
  st.rerun()

if "uploaded_file" not in session_state:
  st.session_state.pop("uploaded_file",None)

with st.form("pdf_form"):
  col1, col2 = st.columns(2)
  reset_form = col1.form_submit_button("Reset Form")
  submit_form = col2.form_submit_button("Show PDF")
  upload_file = st.file_uploader("Browse the PDF file from local drive", type="pdf")
  if reset_form:
    fn_reset_form()
    st.rerun()
  if submit_form and upload_file is not None:
    html_text=""
    doc = fitz.open(stream=upload_file.read(), filetype="pdf")
    for page in doc:
      html_text += page.get_text("html")
    st.markdown(html_text, unsafe_allow_html = True)
      
    
  


  
