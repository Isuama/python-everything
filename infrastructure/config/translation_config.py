# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class TranslationConfig:
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'
    LANGUAGES = ['en', 'si']