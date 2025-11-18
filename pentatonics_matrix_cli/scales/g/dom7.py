# dom7.py — G key center

SCALE_DATA = {
    "g7": [
        {"notes": ("G", "B", "D", "F")},
        {"scales": [

            {"scale": "D minor 6",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "A minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "E minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "B minor 7b5",
             "notes": ("B", "D", "E", "F", "A"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "Eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "G major b2",
             "notes": ("G", "Ab", "B", "D", "E"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "Bb major b2",
             "notes": ("Bb", "C", "D", "F", "G"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "C# major b2",
             "notes": ("C#", "D", "E#", "G#", "A#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 80},

            {"scale": "A major b2",
             "notes": ("A", "Bb", "C#", "E", "F#"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("G", "A", "B", "D#", "F"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("G", "A", "C", "D", "E"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("G", "Ab", "B", "D#", "F"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("G", "Bb", "D#", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
