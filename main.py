import streamlit as st 
from gingerit.gingerit import GingerIt as gt 
import time


style = """
<style>
textarea {
    width : 100%;
    height : 250px;
}
</style>
"""


text_ge = ''
text_generated=''
st.title("Correct Grammatical Errors Using Python : ")

text_given = st.text_area("Enter your content : ",max_chars=500)


st.markdown(f"{style}",unsafe_allow_html=True)

if st.button(" Check it out "):

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    text_generated = gt().parse(text_given)
    my_bar.empty()
    st.subheader("Correct sentence")
    st.write(f"""{text_generated['result']}""")
