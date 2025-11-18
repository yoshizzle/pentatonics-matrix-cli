# utils/loader.py

import importlib
import os
import pkgutil

# Map root spellings to (key_folder, canonical_root_for_scale_data)
ROOT_MAP = {
    "c":  ("c",      "c"),
    "c#": ("csharp", "c#"),
    "db": ("csharp", "c#"),

    "d":  ("d",      "d"),

    "d#": ("dsharp", "d#"),
    "eb": ("dsharp", "d#"),

    "e":  ("e",      "e"),

    "f":  ("f",      "f"),

    "f#": ("fsharp", "f#"),
    "gb": ("fsharp", "f#"),

    "g":  ("g",      "g"),

    "g#": ("gsharp", "g#"),
    "ab": ("gsharp", "g#"),

    "a":  ("a",      "a"),

    "a#": ("bb",     "bb"),
    "bb": ("bb",     "bb"),

    "b":  ("b",      "b"),
}


def parse_key_and_chord(user_input: str):
    """
    Given user input like:
        "Cmaj7"
        "Db7alt"
        "F#min7b5"

    Return:
        (key_folder, chord_key)

    where:
        key_folder = which folder under scales/ to load (e.g. "csharp")
        chord_key  = canonical SCALE_DATA key (e.g. "c#7alt")
    """

    user = user_input.strip().lower()

    # Try longest matches first, so "c#" wins over "c"
    for root in sorted(ROOT_MAP.keys(), key=len, reverse=True):
        if user.startswith(root):
            key_folder, canonical_root = ROOT_MAP[root]
            chord_symbol = user[len(root):]  # e.g. "7alt"

            if not chord_symbol:
                raise ValueError(f"Chord type missing after key '{root}' in '{user_input}'")

            chord_key = f"{canonical_root}{chord_symbol}"  # e.g. "c#7alt"
            return key_folder, chord_key

    raise ValueError(f"Could not determine key center from input '{user_input}'")


def load_key_data(key_folder: str):
    """
    Dynamically load all chord modules inside:

        pentatonics_matrix_cli/scales/<key_folder>/

    and merge their SCALE_DATA dicts into a single dict.
    """

    base_path = f"pentatonics_matrix_cli.scales.{key_folder}"

    try:
        package = importlib.import_module(base_path)
    except ImportError:
        raise ValueError(f"No scale directory found for key folder '{key_folder}'")

    scale_dict = {}

    folder_path = os.path.dirname(package.__file__)

    for _, module_name, is_pkg in pkgutil.iter_modules([folder_path]):
        if is_pkg:
            continue

        module = importlib.import_module(f"{base_path}.{module_name}")

        if not hasattr(module, "SCALE_DATA"):
            continue

        scale_dict.update(module.SCALE_DATA)

    return scale_dict
