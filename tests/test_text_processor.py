from emojify import text_processor

import pytest


def test_removal_stop_words():
    # GIVEN
    text = "Hello, World!.!@#$%&^*(&)_+=|}{:?><"

    # WHEN
    processed_text = text_processor.remove_stop_words(text)

    # THEN
    assert processed_text == ["Hello", "World"]
