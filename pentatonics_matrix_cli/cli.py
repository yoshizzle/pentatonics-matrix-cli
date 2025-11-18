# cli.py

import sys
from pentatonics_matrix_cli.utils.loader import (
    parse_key_and_chord,
    load_key_data,
)


def print_help():
    print("""
Pentatonics Matrix CLI – Usage

Usage:
    pentatonics <ChordName>

Examples:
    pentatonics Cmaj7
    pentatonics cmaj7
    pentatonics C#7alt
    pentatonics Db7alt
    pentatonics F#min7b5

Notes:
    • Key root is case-insensitive (C, c, c#, C#, db, Db, etc.)
    • Chord types are case-insensitive (maj7, MIN7, MinMaj7, etc.)
""")
    sys.exit(0)


def render_table(rows, headers):
    # Compute column widths
    cols = list(zip(headers, *rows))
    widths = [max(len(str(x)) for x in col) for col in cols]

    COLUMN_PADDING = "      "  # adjust spacing between columns
    fmt = COLUMN_PADDING.join("{{:<{}}}".format(w) for w in widths)

    header_line = fmt.format(*headers)
    lines = [header_line]
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
            "   ".join(entry["notes"]),         # extra spacing between notes
            ", ".join(entry["tensions"]),
        ])

    print(render_table(rows, headers))


def main():
    if len(sys.argv) == 1:
        print_help()

    user_input = sys.argv[1].strip()

    try:
        key_folder, chord_key = parse_key_and_chord(user_input)
        scale_dict = load_key_data(key_folder)

        if chord_key not in scale_dict:
            raise KeyError(
                f"Chord '{user_input}' not found. "
                f"(internal lookup key: '{chord_key}' in folder '{key_folder}')"
            )

        print_scales_for_chord(chord_key, scale_dict[chord_key])

    except Exception as e:
        print(f"\nError: {e}\n")
        print_help()


if __name__ == "__main__":
    main()
