from core.ports.translation_port import TranslationPort

class TranslationService:
    def __init__(self, translator: TranslationPort):
        self.translator = translator

    def get_translated_message(self, key: str) -> str:
        return self.translator.translate(key)
