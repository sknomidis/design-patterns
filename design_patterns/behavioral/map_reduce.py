"""Process large datasets with a distributed algorithm.

It consists of two steps:
1. Map: Process input data and generate output.
2. Reduce: Combine all outputs into a final one.
"""

from __future__ import annotations

import concurrent.futures
from typing import Callable, Iterable, Sequence, TypeVar

MapInputType = TypeVar("MapInputType")
MapOutputType = TypeVar("MapOutputType")
ReduceOutputType = TypeVar("ReduceOutputType")


def map_reduce(
    map_function: Callable[[MapInputType], MapOutputType],
    iterable: Iterable[MapInputType],
    reduce_function: Callable[[Sequence[MapOutputType]], ReduceOutputType],
) -> ReduceOutputType:
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    output_per_worker = pool.map(map_function, iterable)
    output_reduced = reduce_function(output_per_worker)
    return output_reduced


# This is a large dataset which can be split into small, independent chunks.
sentences = [
    "The sun sets behind the mountains, painting the sky in shades of orange.",
    "A cat sat on the windowsill, gazing out at the rain.",
    "She danced through the empty streets, her laughter echoing in the night.",
    "The sound of waves crashing against the shore was soothing to her soul.",
    "He opened the door to find an envelope with his name written in elegant handwriting.",
    "In the middle of the forest, there was a small cabin, untouched by time.",
    "The smell of freshly baked bread filled the kitchen, making everyone hungry.",
    "A gentle breeze carried the scent of flowers as they walked through the park.",
    "The stars above were so bright, it felt like the universe was watching them.",
    "He could hear the distant hum of the city, but here it was peaceful.",
    "She opened the book and let the words transport her to another world.",
    "The sound of footsteps echoed through the empty hallway, filling the silence.",
    "The mountain peaks were covered in snow, a perfect winter wonderland.",
    "He couldn't believe his eyes when he saw the treasure chest buried in the sand.",
    "The old clock in the living room ticked away, marking the passing of time.",
    "The street was bustling with life, everyone moving in a hurry to their destinations.",
    "They sat by the campfire, sharing stories and watching the flames dance.",
    "The child smiled as they held out a handful of colorful balloons.",
    "She watched the rain fall softly on the rooftop, feeling a sense of calm.",
    "The old guitar sat in the corner, waiting to be played once more.",
]


# Map: A single task that can be run in parallel.
def split_sentence_into_words(sentence: str) -> list[str]:
    words = sentence.split()
    return words


# Reduce: Combine map outputs into the final one.
def count_words_in_sentences(words_per_sentence: Sequence[Sequence[str]]) -> int:
    word_count = sum(len(words) for words in words_per_sentence)
    return word_count


if __name__ == "__main__":
    word_count = map_reduce(split_sentence_into_words, sentences, count_words_in_sentences)
    print(word_count)
