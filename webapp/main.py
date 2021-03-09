import streamlit as st
import json
from collections import Counter
import main
from translate import Translator
from langdetect import detect
#===========================================#
#        Loads Model and word_to_id         #
#===========================================#
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


#===========================================#
#              Streamlit Code               #
#===========================================#
desc = "Translate from any language to anyother language!"

st.title('Any Language Translator')
st.write(desc)
count_list = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani', 'Bashkir', 'Basque', 'Bengali (Bangla)', 'Bhutani', 'Bihari', 'Bislama', 'Breton', 'Bulgarian', 'Burmese', 'Byelorussian (Belarusian)', 'Cambodian', 'Catalan', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Faeroese', 'Farsi', 'Fiji', 'Finnish', 'French', 'Frisian', 'Galician', 'Gaelic (Scottish)', 'Gaelic (Manx)', 'Georgian', 'German', 'Greek', 'Greenlandic', 'Guarani', 'Gujarati', 'Hausa', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiak', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kashmiri', 'Kazakh', 'Kinyarwanda (Ruanda)', 'Kirghiz', 'Kirundi (Rundi)', 'Korean', 'Kurdish', 'Laothian', 'Latin', 'Latvian (Lettish)', 'Limburgish ( Limburger)', 'Lingala', 'Lithuanian', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Moldavian', 'Mongolian', 'Nauru', 'Nepali', 'Norwegian', 'Occitan', 'Oriya', 'Oromo (Afan, Galla)', 'Pashto (Pushto)', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Rhaeto-Romance', 'Romanian', 'Russian', 'Samoan', 'Sangro', 'Sanskrit', 'Serbian', 'Serbo-Croatian', 'Sesotho', 'Setswana', 'Shona', 'Sindhi', 'Sinhalese', 'Siswati', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili (Kiswahili)', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Volapük', 'Welsh', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
#from_lang = st.selectbox('Input Language',('Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani', 'Bashkir', 'Basque', 'Bengali (Bangla)', 'Bhutani', 'Bihari', 'Bislama', 'Breton', 'Bulgarian', 'Burmese', 'Byelorussian (Belarusian)', 'Cambodian', 'Catalan', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Faeroese', 'Farsi', 'Fiji', 'Finnish', 'French', 'Frisian', 'Galician', 'Gaelic (Scottish)', 'Gaelic (Manx)', 'Georgian', 'German', 'Greek', 'Greenlandic', 'Guarani', 'Gujarati', 'Hausa', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiak', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kashmiri', 'Kazakh', 'Kinyarwanda (Ruanda)', 'Kirghiz', 'Kirundi (Rundi)', 'Korean', 'Kurdish', 'Laothian', 'Latin', 'Latvian (Lettish)', 'Limburgish ( Limburger)', 'Lingala', 'Lithuanian', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Moldavian', 'Mongolian', 'Nauru', 'Nepali', 'Norwegian', 'Occitan', 'Oriya', 'Oromo (Afan, Galla)', 'Pashto (Pushto)', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Rhaeto-Romance', 'Romanian', 'Russian', 'Samoan', 'Sangro', 'Sanskrit', 'Serbian', 'Serbo-Croatian', 'Sesotho', 'Setswana', 'Shona', 'Sindhi', 'Sinhalese', 'Siswati', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili (Kiswahili)', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Volapük', 'Welsh', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'))
to_lang =st.selectbox('Output Language',('Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani', 'Bashkir', 'Basque', 'Bengali (Bangla)', 'Bhutani', 'Bihari', 'Bislama', 'Breton', 'Bulgarian', 'Burmese', 'Byelorussian (Belarusian)', 'Cambodian', 'Catalan', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Faeroese', 'Farsi', 'Fiji', 'Finnish', 'French', 'Frisian', 'Galician', 'Gaelic (Scottish)', 'Gaelic (Manx)', 'Georgian', 'German', 'Greek', 'Greenlandic', 'Guarani', 'Gujarati', 'Hausa', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiak', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kashmiri', 'Kazakh', 'Kinyarwanda (Ruanda)', 'Kirghiz', 'Kirundi (Rundi)', 'Korean', 'Kurdish', 'Laothian', 'Latin', 'Latvian (Lettish)', 'Limburgish ( Limburger)', 'Lingala', 'Lithuanian', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Moldavian', 'Mongolian', 'Nauru', 'Nepali', 'Norwegian', 'Occitan', 'Oriya', 'Oromo (Afan, Galla)', 'Pashto (Pushto)', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Rhaeto-Romance', 'Romanian', 'Russian', 'Samoan', 'Sangro', 'Sanskrit', 'Serbian', 'Serbo-Croatian', 'Sesotho', 'Setswana', 'Shona', 'Sindhi', 'Sinhalese', 'Siswati', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili (Kiswahili)', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Volapük', 'Welsh', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'))

user_input = st.text_input('Enter the text to be translated')

index = 0
for i in range(len(count_list)):
    if to_lang == count_list[i]:
        index =i
        break
abb_list = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'ba', 'eu', 'bn', 'dz', 'bh', 'bi', 'br', 'bg', 'my', 'be', 'km', 'ca', 'zh', 'zh', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fo', 'fa', 'fj', 'fi', 'fr', 'fy', 'gl', 'gd', 'gv', 'ka', 'de', 'el', 'kl', 'gn', 'gu', 'ha', 'he', 'hi', 'hu', 'is', 'id', 'ia', 'ie', 'iu', 'ik', 'ga', 'it', 'ja', 'ja', 'kn', 'ks', 'kk', 'rw', 'ky', 'rn', 'ko', 'ku', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mo', 'mn', 'na', 'ne', 'no', 'oc', 'or', 'om', 'ps', 'pl', 'pt', 'pa', 'qu', 'rm', 'ro', 'ru', 'sm', 'sg', 'sa', 'sr', 'sh', 'st', 'tn', 'sn', 'sd', 'si', 'ss', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'bo', 'ti', 'to', 'ts', 'tr', 'tk', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vo', 'cy', 'wo', 'xh', 'yi', 'yo', 'zu']

if st.button('Translate'):
    print(abb_list[index])
    generated_text = main.transalation_lang(abb_list[index],user_input)
    
    st.write(generated_text)

def transalation_lang(output_language,text):
    translator= Translator(to_lang=output_language)
    translation = translator.translate(text)
    return translation
    