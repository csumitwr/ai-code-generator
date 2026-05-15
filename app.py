# Chunk 1
import streamlit as st
from utils import generate_code


# Chunk 2
st.set_page_config(
    page_title="AI Code Generator",
    page_icon="💻",
    layout="wide"
)


# Chunk 3
def load_css():
    with open("styles.css") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# Chunk 4
st.markdown(
    """
    <h1 class="main-title">
        AI Code Generator
    </h1>
    """,
    unsafe_allow_html=True
)


# Chunk 5
languages = [
    "Python",
    "JavaScript",
    "Java",
    "C",
    "C++"
]


# Chunk 6
left_column, right_column = st.columns(
    [4, 1.3],
    vertical_alignment="bottom"
)


with left_column:

    selected_language = st.selectbox(
        "Language",
        languages
    )


with right_column:

    generate_button = st.button(
        "Generate Code",
        use_container_width=True
    )


# Chunk 7
user_prompt = st.text_area(
    "Prompt",
    height=420,
    placeholder="Ask any coding question..."
)


# Chunk 8
if generate_button:

    if user_prompt.strip() == "":

        st.warning("Please enter a coding request.")

    else:

        with st.spinner("Generating code..."):

            response = generate_code(
                user_prompt,
                selected_language
            )


# Chunk 9
        if "EXPLANATION:" in response:

            code_part, explanation_part = response.split(
                "EXPLANATION:",
                1
            )

        else:

            code_part = response
            explanation_part = "No explanation generated."


# Chunk 10
        st.markdown("## Generated Code")

        st.code(
            code_part,
            language=selected_language.lower()
        )


# Chunk 11
        st.markdown("## Explanation")

        st.markdown(
            f"""
            <div class="explanation-box">
                {explanation_part}
            </div>
            """,
            unsafe_allow_html=True
        )