#api_operations.py
import requests

# Your existing code for get_response function

# def get_translation(word, target_language):
#     api_url = f"https://api.mymemory.translated.net/get?q={word}&langpair=en|{target_language}"
#     response = requests.get(api_url)
#     translation_data = response.json()
#     translated_text = translation_data.get("responseData", {}).get("translatedText", "").lstrip('*-: ').lower()
#     target_language =target_language.lower() 
#     if target_language == translated_text:
#         return f"Translation not found"
#     else:
#         return translated_text

def get_translation(word):
    api_url = f"https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=en&tl=vi&hl=en-US&dt=t&dt=bd&dj=1&source=bubble&q={word}"
    response = requests.get(api_url)
    translation_data = response.json()
    translated_text = translation_data["sentences"][0]["trans"]
    return translated_text

