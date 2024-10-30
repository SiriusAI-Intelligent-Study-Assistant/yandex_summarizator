# -*- coding: utf-8 -*-

from .models.mistral_ai.api import MistralAI_API
from .models.rut5_base_absum.api import RuT5_API
from .models.mistral_ai.gen_prompt import prompt
import logging


class Summarizer:
    """
    A class for managing summarization models
    """

    def __init__(self, model_name: str, model_api_key: str, _device: str) -> None:
        match model_name:
            case "llm":
                self.model = MistralAI_API(model_api_key)
                self.summarize = self.summarize_with_llm
                logging.info("Loaded API for working with LLM: MistralLarge")

            case "rut5":
                self.model = RuT5_API(_device)
                self.summarize = self.summarize_with_hf
                logging.info("Loaded model for summarization with HuggingFace: cointegrated/rut5-base-absum")

            case _: raise NameError(f"Model <{model_name}> not found!")
        
    def summarize_with_llm(self, text: str, text_volume: int = 5, bullet_points: int = 0, **kwargs) -> str:
        logging.info("Summarizing the text...")
        return self.model.summarize_with_llm(prompt(text_volume, bullet_points) + text)
    
    def summarize_with_hf(self, text: str, n_words=None, compression=None, 
                          max_length=1000, num_beams=3, do_sample=False, 
                          repetition_penalty=10.0, **kwargs):
        
        logging.info("Summarizing the text...")
        return self.model.summarize_with_hf(text, n_words, compression, 
                                            max_length, num_beams, do_sample, 
                                            repetition_penalty)