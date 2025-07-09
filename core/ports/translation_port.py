from abc import ABC, abstractmethod

class TranslationPort(ABC):
    @abstractmethod
    def translate(self, message: str) -> str:
        pass
