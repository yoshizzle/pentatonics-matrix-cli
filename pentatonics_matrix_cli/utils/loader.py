# utils/loader.py

import importlib
import os
import pkgutil


# Mapping of all recognized input key names → folder names
VALID_KEYS = {
    "c": "c",
    "c#": "csharp", "db": "csharp",
    "d": "d",
    "d#": "dsharp", "eb": "dsharp",
    "e": "e",
    "f": "f",
    "f#": "fsharp", "gb": "fsharp",
    "g": "g",
    "g#": "gsharp", "ab": "gsharp",
    "a": "a",
    "a#": "bb", "bb": "bb",
    "b": "b",
}


def parse_key_and_chord(user_input: str):
    """
    Return:
        (key_string, key_folder, chord_symbol)

    Example:
        "C#Maj7#11" → ("c#", "csharp", "maj7#11")
    """

    user_input = user_input.strip()

    # Try longest match first
    for key in sorted(VALID_KEYS.keys(), key=len, reverse=True):
        if user_input.lower().startswith(key):
            key_string = key      # e.g. "c#"
            key_folder = VALID_KEYS[key]   # e.g. "csharp"
            chord_symbol = user_input[len(key):]

            if not chord_symbol:
                raise ValueError(f"Chord type missing after key '{key}' in '{user_input}'")

            return key_string, key_folder, chord_symbol

    raise ValueError(f"Could not determine key center from input '{user_input}'")

def load_key_data(key_folder: str):
    """
    Dynamically load all chord modules inside:
        pentatonics_matrix_cli/scales/<key_folder>/
    """

    base_path = f"pentatonics_matrix_cli.scales.{key_folder}"

    try:
        package = importlib.import_module(base_path)
    except ImportError:
        raise ValueError(f"No scale directory found for key '{key_folder}'")

    scale_dict = {}

    folder_path = os.path.dirname(package.__file__)

    for _, module_name, is_pkg in pkgutil.iter_modules([folder_path]):
        if is_pkg:
            continue

        module = importlib.import_module(f"{base_path}.{module_name}")

        if not hasattr(module, "SCALE_DATA"):
            continue

        # ✔ Ensure chord keys are lowercase for matching CLI input
        lowered = {k.lower(): v for k, v in module.SCALE_DATA.items()}
        scale_dict.update(lowered)

    return scale_dict