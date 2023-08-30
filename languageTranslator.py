from translate import Translator

language= ['french','italian ','Russian','German']
language.append('Hindi')


text= input('what text would you like to translate? >>')

for language in language:
    translator= Translator(provider='mymemory',from_lang='en',to_lang=language)
    translation = translator.translate(text)
    print(f'{language}:{translation}')


