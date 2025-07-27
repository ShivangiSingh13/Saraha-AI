import streamlit as st

# Translation dictionary
translations = {
    "hi": {
        "Select your category:": "अपनी श्रेणी चुनें:",
        "Recommended Government Schemes:": "अनुशंसित सरकारी योजनाएं:",
        "Your Feedback Helps Us Improve:": "आपकी प्रतिक्रिया हमें सुधारने में मदद करती है:",
        "Let us know how we can help you better:": "हमें बताएं कि हम आपकी कैसे मदद कर सकते हैं:",
        "Submit Feedback": "प्रतिक्रिया सबमिट करें",
        "Thank you for your valuable input!": "आपके बहुमूल्य सुझाव के लिए धन्यवाद!",
        "About this App": "इस ऐप के बारे में",
        "This digital companion helps citizens explore and understand government schemes based on their profile. We aim to bridge the awareness gap and make social welfare accessible to all.": 
        "यह डिजिटल साथी नागरिकों को उनकी प्रोफ़ाइल के आधार पर सरकारी योजनाओं को समझने और खोजने में मदद करता है। हम जागरूकता की खाई को पाटने और सामाजिक कल्याण को सभी के लिए सुलभ बनाने का लक्ष्य रखते हैं।",
        "Choose your language / अपनी भाषा चुनें:": "अपनी भाषा चुनें:",
        "Women": "महिला",
        "Farmers": "किसान",
        "Students": "छात्र"
    }
}

# Manual translate function using dictionary
def translate_text(text, lang):
    if lang == "en":
        return text
    return translations.get(lang, {}).get(text, text)

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

# App UI
st.set_page_config(page_title="Digital Companion for Social Welfare", layout="centered")
st.title("🤝 Digital Companion for Social Welfare")

# Language selection
lang = st.selectbox("Choose your language / अपनी भाषा चुनें:", list(languages.keys()))
dest_lang = languages[lang]

# User type selection
user_keys = list(schemes.keys())
translated_user_keys = [translate_text(key, dest_lang) for key in user_keys]
selected_index = st.radio(translate_text("Select your category:", dest_lang), translated_user_keys, index=0)
user_type = user_keys[translated_user_keys.index(selected_index)]  # Get original key

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
        "This digital companion helps citizens explore and understand government schemes based on their profile. We aim to bridge the awareness gap and make social welfare accessible to all.", dest_lang))
