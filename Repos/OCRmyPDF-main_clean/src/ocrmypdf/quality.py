                                              
                                  

"""Utilities to measure OCR quality."""

from __future__ import annotations

import re
from collections.abc import Iterable


class OcrQualityDictionary:
                                                             

    def __init__(self, *, wordlist: Iterable[str]):
                   
        self.dictionary = set(wordlist)

    def measure_words_matched(self, ocr_text: str) -> float:
                   
        text = re.sub(r"[0-9_]+", ' ', ocr_text)
        text = re.sub(r'\W+', ' ', text)
        text_words_list = re.split(r'\s+', text)
        text_words = {w for w in text_words_list if len(w) >= 3}

        matches = 0
        for w in text_words:
            if w in self.dictionary or (
                w != w.lower() and w.lower() in self.dictionary
            ):
                matches += 1
        if matches > 0:
            hit_ratio = matches / len(text_words)
        else:
            hit_ratio = 0.0
        return hit_ratio
