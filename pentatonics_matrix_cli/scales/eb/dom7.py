# dom7.py — Eb key center

SCALE_DATA = {
    "eb7": [
        {"notes": ("Eb", "G", "Bb", "Db")},
        {"scales": [

            {"scale": "bb minor 6",
             "notes": ("Bb", "Db", "Eb", "F", "G"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "f minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "c minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "g minor 7b5",
             "notes": ("G", "Bb", "C", "Db", "F"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "gb minor",
             "notes": ("Gb", "A", "B", "Db", "E"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "eb major b2",
             "notes": ("Eb", "Fb", "G", "Bb", "C"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "gb major b2",
             "notes": ("Gb", "G", "Bb", "Db", "Eb"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "a major b2",
             "notes": ("A", "Bb", "C#", "E", "F#"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 80},

            {"scale": "c major b2",
             "notes": ("C", "Db", "E", "G", "A"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Eb", "F", "G", "B", "C#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Eb", "F", "Ab", "Bb", "C"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Eb", "E", "G", "A", "C"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Eb", "Gb", "A", "C", "Db"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
