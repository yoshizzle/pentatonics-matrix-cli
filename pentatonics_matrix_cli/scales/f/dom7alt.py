# dom7alt.py — F key center

SCALE_DATA = {
    "f7alt": [
        {"notes": ("F", "A", "Cb", "C#", "Eb", "Gb", "Ab")},
        {"scales": [

            {"scale": "f whole tone",
             "notes": ("F", "G", "A", "B", "C#", "D#", "F"),
             "tensions": ("r", "9", "3", "#11", "#5", "b7", "r"),
             "order": 10},

            {"scale": "d major b6",
             "notes": ("D", "F#", "G", "A", "B"),
             "tensions": ("13", "3", "b5", "#5", "b7"),
             "order": 20},

            {"scale": "a minor 6",
             "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("3", "5", "13", "b7", "r"),
             "order": 30},

            {"scale": "eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Cb"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 40},

            {"scale": "bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "Fb", "Ab"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 50},

            {"scale": "db minor 6",
             "notes": ("Db", "Fb", "Gb", "Ab", "Bb"),
             "tensions": ("b9", "3", "b5", "#5", "b7"),
             "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F", "G", "A", "C#", "D#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F", "G", "Bb", "C", "D"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F", "Gb", "A", "B", "D"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F", "Ab", "B", "D", "Eb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
