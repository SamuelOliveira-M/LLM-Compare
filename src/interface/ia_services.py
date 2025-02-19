# src/models/ia_service.py
from abc import ABC, abstractmethod

class IAService(ABC):
    
  @abstractmethod
  def gerar_resposta(self, texto: str) -> str:
    """Método abstrato que deve ser implementado pelas subclasses"""
    pass

