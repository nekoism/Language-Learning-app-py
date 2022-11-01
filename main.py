from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from googletrans import Translator, constants 
# Google Translate API need to be instal as pip install googletrans==3.1.0a0, before this uninstall the old googletrans by pip unistall gooletrans
from pprint import pprint
translator = Translator()
app = Flask(__name__)
languageCodes = LANGUAGES = {
'afrikaans': 'af',
'albanian': 'sq',
'amharic': 'am',
'arabic': 'ar',
'armenian': 'hy',
'azerbaijani': 'az',
'basque': 'eu',
'belarusian': 'be',
'bengali': 'bn',
'bosnian': 'bs',
'bulgarian': 'bg',
'catalan': 'ca',
'cebuano': 'ceb',
'chichewa': 'ny',
'chinese (simplified)': 'zh-cn',
'chinese': 'zh-tw',
'corsican': 'co',
'croatian': 'hr',
'czech': 'cs',
'danish': 'da',
'dutch': 'nl',
'english': 'en',
'esperanto': 'eo',
'estonian': 'et',
'filipino': 'tl',
'finnish': 'fi',
'french': 'fr',
'frisian': 'fy',
'galician': 'gl',
'georgian': 'ka',
'german': 'de',
'greek': 'el',
'gujarati': 'gu',
'haitian creole': 'ht',
'hausa': 'ha',
'hawaiian': 'haw',
'hebrew': 'iw',
'hindi': 'hi',
'hmong': 'hmn',
'hungarian': 'hu',
'icelandic': 'is',
'igbo': 'ig',
'indonesian': 'id',
'irish': 'ga',
'italian': 'it',
'japanese': 'ja',
'javanese': 'jw',
'kannada': 'kn',
'kazakh': 'kk',
'khmer': 'km',
'korean': 'ko',
 'kurdish (kurmanji)': 'ku',
'kyrgyz': 'ky',
'lao': 'lo',
'latin': 'la',
'latvian': 'lv',
'lithuanian': 'lt',
'luxembourgish': 'lb',
'macedonian': 'mk',
'malagasy': 'mg',
'malay': 'ms',
'malayalam': 'ml',
'maltese': 'mt',
'maori': 'mi',
'marathi': 'mr',
'mongolian': 'mn',
'myanmar (burmese)': 'my',
'nepali': 'ne',
'norwegian': 'no',
'pashto': 'ps',
'persian': 'fa',
'polish': 'pl',
'portuguese': 'pt',
'punjabi': 'pa',
'romanian': 'ro',
'russian': 'ru',
'samoan': 'sm',
'scots gaelic': 'gd',
'serbian': 'sr',
'sesotho': 'st',
'shona': 'sn',
'sindhi': 'sd',
'sinhala': 'si',
'slovak': 'sk',
'slovenian': 'sl',
'somali': 'so',
'spanish': 'es',
'sundanese': 'su',
'swahili': 'sw',
'swedish': 'sv',
'tajik': 'tg',
'tamil': 'ta',
'telugu': 'te',
'thai': 'th',
'turkish': 'tr',
'ukrainian': 'uk',
'urdu': 'ur',
'uzbek': 'uz',
'vietnamese': 'vi',
'welsh': 'cy',
'xhosa': 'xh',
'yiddish': 'yi',
'yoruba': 'yo',
'zulu': 'zu',
'Filipino': 'fil',
'Hebrew': 'he',
}

global englishQuote 
global anotherLanguage
def get_quote(language):
    #returns the quote from the api
    res = requests.get('https://animechan.vercel.app/api/random')
    response = json.loads(res.text)
    translation = translator.translate(response['quote'],dest=language)
    
    englishQuote = translation.origin
    
    anotherLanguage = translation.text
    return f"{translation.text} ({translation.dest})"
    
"""
Try to add random language learning which Will be use to learn a different language
"""
# @app.route('/home')
# def home():
#   retun
@app.route('/')
def index():  
  return render_template('index.html')
@app.route('/language')
def language():
  language = request.args.get('language')
  if language.lower() in languageCodes:
    return render_template('language.html', languageQuote=get_quote(languageCodes.get(language.lower())))
  else: 
    return render_template('index.html',inc="incorrect language try again")
  
@app.route("/answer")
def answer():
  name = request.args.get('answer')
  if(name == englishQuote):
    return render_template("correctAnswer.html", realAnswer=englishQuote)
  else:
    userCheck = ""
    userAnwser = name.split(' ');
    realAnswer = englishQuote.split(' ');
    global check
    if len(userAnwser) < len(realAnswer):
        userCheck = "I believe You have not tried it so please try again"
        check = False
    else: 
        userCheck = "Hint check if you placed these words in the sentence: "
        check = True
    for i in range(len(realAnswer)):
      if check:
        if userAnwser[i] != realAnswer[i]:
            userCheck += realAnswer[i] + " ";
    return render_template("wrongAnswer.html", userCheck=userCheck,languageQuote=anotherLanguage)
app.run(host='0.0.0.0', port=81)
