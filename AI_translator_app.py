# source language and target language lists
# prompt
# translation function
# add a translate button -> download button
# OpenAI API Playground


import streamlit as st
from langchain_community.llms import OpenAI

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
