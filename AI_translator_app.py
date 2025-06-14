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
