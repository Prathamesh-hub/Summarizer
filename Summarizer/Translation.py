def translate1(text, language):

    from deep_translator import GoogleTranslator
    print('Translating...',end='')
    converted = str(text)
    splitarray = converted.split("\n")
    translation=""
    for str1 in splitarray:
        to_translate = str1
        translated = GoogleTranslator(source='auto', target=language).translate(to_translate)
        translation += translated
        translation +="\n"

    print('Done')
    return translation