import streamlit as st

def translate_text(text, dest):
    return text

# Language options
languages = {
    "English": "en",
    "Hindi": "hi"
}

# Scheme database
schemes = {
    "Women": [
        {"name": "Beti Bachao, Beti Padhao", "desc": "Promotes education for girls."},
        {"name": "PM Ujjwala Yojana", "desc": "LPG connection for women below poverty line."}
    ],
    "Farmers": [
        {"name": "PM-KISAN", "desc": "Income support to farmers."},
        {"name": "Soil Health Card", "desc": "Provides information on nutrient status of soil."}
    ],
    "Students": [
        {"name": "National Scholarship Portal", "desc": "Scholarships for meritorious students."},
        {"name": "Skill India Mission", "desc": "Enhances employability of youth."}
    ]
}

# Translate text function
def translate_text(text, dest):
    if dest == "en":
        return text
    try:
        return translator.translate(text, dest=dest).text
    except:
        return text  # fallback in case of API failure

# App title
st.set_page_config(page_title="Digital Companion for Social Welfare", layout="centered")
st.title("🤝 Digital Companion for Social Welfare")

# Language selection
lang = st.selectbox("Choose your language / अपनी भाषा चुनें:", list(languages.keys()))
dest_lang = languages[lang]

# User type selection
user_type = st.radio(translate_text("Select your category:", dest_lang), list(schemes.keys()))

# Show schemes
st.subheader(translate_text("Recommended Government Schemes:", dest_lang))
for scheme in schemes[user_type]:
    st.markdown(f"**{translate_text(scheme['name'], dest_lang)}**")
    st.markdown(f"*{translate_text(scheme['desc'], dest_lang)}*")
    st.divider()

# Feedback
st.subheader(translate_text("Your Feedback Helps Us Improve:", dest_lang))
feedback = st.text_area(translate_text("Let us know how we can help you better:", dest_lang))
if st.button(translate_text("Submit Feedback", dest_lang)):
    st.success(translate_text("Thank you for your valuable input!", dest_lang))

# About section
with st.expander(translate_text("About this App", dest_lang)):
    st.write(translate_text(
        "This digital companion helps citizens explore and understand government schemes based on their profile."
        " We aim to bridge the awareness gap and make social welfare accessible to all.", dest_lang))
