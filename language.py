from translate import Translator
from langdetect import detect

def transalation_lang(output_language,text):
    translator= Translator(to_lang=output_language)
    translation = translator.translate(text)


    return translation
    
