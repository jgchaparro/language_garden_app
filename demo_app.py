import streamlit as st
from openai import OpenAI, BadRequestError
from utils import available_models, lang_name_to_code, lang_code_to_name

st.set_page_config(page_title="Language Garden", page_icon="🌲", layout="wide")

# Streaming helper
def stream_text(text):
    for char in text:
        yield char

# Save previous parameters
with st.sidebar:
    st.title("Language garden", anchor = "right")
    # st.image("assets/image.png", use_column_width=True) 
    # Set main language
    main_language_name = st.selectbox(
        "Select the main language:",
        [lang_code_to_name[code] for code in available_models.keys()]
    )
    st.session_state.main_language_name = main_language_name
    st.session_state.main_language_code = lang_name_to_code[main_language_name]

    # Translation settings
    available_pairs_codes = [pair for pair in available_models[st.session_state.main_language_code].keys()]
    available_pairs_names = [f"{lang_code_to_name[pair.split('-')[0]]} → {lang_code_to_name[pair.split('-')[1]]}" for pair in available_pairs_codes]
    st.session_state.available_pairs_names = available_pairs_names

    translation_pair = st.selectbox(
        "Select the translation pair:",
        available_pairs_names
    )
    st.session_state.translation_pair = translation_pair
    translation_pair_list = translation_pair.split(' → ')
    origin_language_name, target_language_name = translation_pair_list[0], translation_pair_list[1]
    st.session_state.origin_language_name = origin_language_name
    st.session_state.target_language_name = target_language_name
    st.session_state.origin_language_code = lang_name_to_code[origin_language_name]
    st.session_state.target_language_code = lang_name_to_code[target_language_name]

    # Set endpoint
    endpoint = available_models[st.session_state.main_language_code][f"{st.session_state.origin_language_code}-{st.session_state.target_language_code}"]

    if st.button("Clear conversation"):
        st.session_state.messages = []

st.session_state.client = OpenAI(
    base_url = endpoint,
    api_key = "Malaga",
)

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if to_translate := st.chat_input("Input a sentence to translate..."):
    st.session_state.messages.append({"role": "user", "content": to_translate})
    with st.chat_message("user"):
        st.markdown(to_translate)

    with st.chat_message("assistant"):
        try:
            chat_completion = st.session_state.client.chat.completions.create(
                model="tgi",
                messages=[
                {
                    "role": "user",
                    "content": f"Translate the following sentence from Greek to Tsakonian: {to_translate}"
                }
            ],
                temperature = 0,
                max_tokens = 150,
                # stream = False,
                seed = None,
            )

            translation = chat_completion.choices[0].message.content.replace('Translation to Tsakonian: ', '')
        except BadRequestError:
            translation = "The request was not processed, probably due to the server not being active. Please, try again later."
        
        st.write_stream(stream_text(translation))
        st.session_state.messages.append({"role": "assistant", "content": translation})