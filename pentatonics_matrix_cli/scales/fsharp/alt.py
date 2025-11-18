# dom7alt.py — F# key center

SCALE_DATA = {
    "f#7alt": [
        {"notes": ("F#", "A#", "C", "Cx", "E", "G", "G#")},
        {"scales": [

            {"scale": "f# whole tone",
             "notes": ("F#", "G#", "A#", "B#", "Cx"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "d# major b6",
             "notes": ("D#", "F#", "G#", "A#", "C#"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "a# minor 6",
             "notes": ("A#", "C#", "D#", "E#", "G#"),
             "tensions": ("b9", "3", "b5", "#5", "7"),
             "order": 30},

            {"scale": "eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 40},

            {"scale": "eb minor 6",
             "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 50},

            {"scale": "bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "Fb", "Ab"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F#", "G#", "A#", "D", "E"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F#", "G#", "B", "C#", "D#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F#", "G", "A#", "C", "E"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F#", "A", "C", "E", "E#"),
             "tensions": ("r", "#9", "b5", "13", "7"),
             "order": 130}
        ]}
    ]
}
