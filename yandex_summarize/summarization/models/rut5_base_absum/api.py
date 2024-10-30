# -*- coding: utf-8 -*-

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import logging


class RuT5_API:
    """
    Class for interaction with local summarization model:
    https://huggingface.co/cointegrated/rut5-base-absum

    """

    def __init__(self, device: str, _model_name: str = 'cointegrated/rut5-base-absum') -> None:
        self.model = T5ForConditionalGeneration.from_pretrained(_model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(_model_name)

        self.model.cuda() if device == "cuda" else "cpu"
        self.model.eval()
        
    def summarize_with_hf(self, text, n_words=None, compression=None, 
                          max_length=1000, num_beams=3, do_sample=False, 
                          repetition_penalty=10.0) -> str:
        """
        Summarize the text
        The following parameters are mutually exclusive:
        - n_words (int) is an approximate number of words to generate.
        - compression (float) is an approximate length ratio of summary and original text.
        """

        if n_words:
            text = '[{}] '.format(n_words) + text
        elif compression:
            text = '[{0:.1g}] '.format(compression) + text

        x = self.tokenizer(text, return_tensors='pt', padding=True).to(self.model.device)
        with torch.inference_mode():
            out = self.model.generate(
                **x, 
                max_length=max_length, num_beams=num_beams, 
                do_sample=do_sample, repetition_penalty=repetition_penalty, 
            )

        logging.info(f"Summarization has been successfully completed! Model: 'cointegrated/rut5-base-absum'; HuggingFace.")
        return self.tokenizer.decode(out[0], skip_special_tokens=True)
