# cli.py

import sys
from pentatonics_matrix_cli.utils.loader import (
    parse_key_and_chord,
    load_key_data
)


def print_help():
    print("""
Pentatonics Matrix CLI – Usage

Usage:
    pentatonics <KeyChord>

Examples:
    pentatonics CMaj7
    pentatonics Ab7alt
    pentatonics F#min7b5
    pentatonics Dbmaj7#11

Valid key centers:
    C  C#  Db  D  Eb  E  F  F#  Gb  G  Ab  A  Bb  B

Valid chord types:
    maj7           maj7#11       maj7#5       maj7b5
    min7           min6          minmaj7
    min7b5         min7b5nat9
    7              7#11          7b9sus
    7nat9b13       alt
""")
    sys.exit(0)


# ----------------------------------------------------
# Simple built-in table formatter (no dependencies)
# ----------------------------------------------------
def render_table(rows, headers):
    cols = list(zip(headers, *rows))
    widths = [max(len(str(x)) for x in col) for col in cols]
    fmt = "    ".join("{{:<{}}}".format(w) for w in widths)

    lines = [fmt.format(*headers)]
    header_line = fmt.format(*headers)
    lines.append("-" * len(header_line))

    for r in rows:
        lines.append(fmt.format(*r))

    return "\n".join(lines)


def print_scales_for_chord(chord_key, chord_data):
    chord_notes = chord_data[0]["notes"]
    scale_list = chord_data[1]["scales"]

    print(f"\n=== {chord_key} ===")
    print(f"Chord tones: {', '.join(chord_notes)}\n")

    headers = ["Scale", "Notes", "Tensions"]
    rows = []

    for entry in scale_list:
        rows.append([
            entry["scale"],
            "   ".join(entry["notes"]),
            ", ".join(entry["tensions"])
        ])

    print(render_table(rows, headers))


def main():
    if len(sys.argv) == 1:
        print_help()

    user_input = sys.argv[1].strip()

    try:
        key_string, key_folder, chord_symbol = parse_key_and_chord(user_input)
        scale_dict = load_key_data(key_folder)

        chord_key = (key_string + chord_symbol).lower()

        if chord_key not in scale_dict:
            raise KeyError(f"Chord '{user_input}' ({chord_key}) not found in key '{key_folder}'")

        print_scales_for_chord(chord_key, scale_dict[chord_key])

    except Exception as e:
        print(f"\nError: {e}\n")
        print_help()


if __name__ == "__main__":
    main()
