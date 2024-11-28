import streamlit as st
import requests
import json

st.set_page_config(page_title="Language Garden", page_icon="🌲", layout="wide")

# Set language codes
lang_name_to_code = {
    'Tsakonian': 'tsd', 
    'Fala': 'fax',
    'Spanish' : 'spa',
    'English' : 'eng',
    'Greek' : 'ell',
    }

lang_code_to_name = {v: k for k, v in lang_name_to_code.items()}

available_gardens = [
    'tsd', 'fax'
]

available_models = [
    # from, to, endpoint
    ('ell', 'tsd', 'https://api-inference.huggingface.co/models/vasudevgupta/llm-tsd'),
]

# Streaming helper
def stream_text(text):
    for char in text:
        yield char

with st.sidebar:
    st.title("Language garden", anchor = "right")
    # st.image("assets/image.png", use_column_width=True) 
    # Set main language
    main_language_name = st.selectbox(
        "Select the main language:",
        [lang_code_to_name[code] for code in available_gardens]
    )
    st.session_state.main_language_name = main_language_name
    st.session_state.main_language_code = lang_name_to_code[main_language_name]

    # Translation settings
    available_pairs = [f"{lang_code_to_name[pair[0]]} → {lang_code_to_name[pair[1]]}" for pair in available_models]
    st.session_state.available_pairs = available_pairs

    translation_pair = st.selectbox(
        "Select the translation pair:",
        available_pairs
    )
    st.session_state.translation_pair = translation_pair
    translation_pair = translation_pair.split(' → ')
    origin_language_name, target_language_name = translation_pair[0], translation_pair[1]
    st.session_state.origin_language_name = origin_language_name
    st.session_state.target_language_name = target_language_name
    st.session_state.origin_language_code = lang_name_to_code[origin_language_name]
    st.session_state.target_language_code = lang_name_to_code[target_language_name]

    # Set endpoint
    endpoint = 'https://rgoyhhcmfy2sv9od.us-east-1.aws.endpoints.huggingface.cloud'

    if st.button("Clear conversation"):
        st.session_state.messages = []

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if to_translate := st.chat_input(f"Input a sentence to translate from {st.session_state.origin_language_name} to {st.session_state.target_language_name}"):
    st.session_state.messages.append({"role": "user", "content": to_translate})
    with st.chat_message("user"):
        st.markdown(to_translate)

    with st.chat_message("assistant"):
        with st.spinner("Translating..."):
            response = requests.get(endpoint, params={'text': to_translate})
            translation = json.loads(response.text)['translation']
        st.write_stream(stream_text(translation))
        st.session_state.messages.append({"role": "assistant", "content": translation})