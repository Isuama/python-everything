from flask_babel import _
from core.ports.translation_port import TranslationPort

class FlaskBabelAdapter(TranslationPort):
    def translate(self, message: str) -> str:
        return _(message)
