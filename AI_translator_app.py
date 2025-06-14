# source language and target language lists
# prompt
# translation function
# add a translate button -> download button
# OpenAI API Playground


import streamlit as st
from langchain.llms import OpenAI

llms = OpenAI(openai_api_key="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")

st.title("AI Translator")

st.divider()

input_text = st.text_area("Enter the text you want to translate: ")

source_language = st.selectbox("Select source language", ["English", "Spanish", "German", "Tamil", "Hindi"])
target_language = st.selectbox("Select target language", ["English", "Spanish", "German", "Tamil", "Hindi"])

def translate_text(input_text, source_language, target_language):
    prompt = f"Translate this from {source_language} to {target_language}: {input_text}"
    translation = llms(prompt)
    return translation


if st.button("Translate"):
    if input_text:
        translation = translate_text(input_text, source_language, target_language)
        st.write("Translation", translation)

        st.download_button(
            label = "Download translation as a .txt file",
            data = translation,
            file_name = "translation.txt",
            mime = "text/plain"
        )

else:
    st.write("Please enter some text to translate.")