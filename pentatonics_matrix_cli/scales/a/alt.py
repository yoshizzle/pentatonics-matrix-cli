# alt.py — A key center

SCALE_DATA = {
    "a7alt": [
        {"notes": ("A", "C#", "E", "F", "G#", "B", "C")},
        {"scales": [

            {"scale": "A whole tone",
             "notes": ("A", "B", "C#", "D#", "F"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "F# major b6",
             "notes": ("F#", "A#", "B", "C#", "E"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "B minor 6",
             "notes": ("B", "D", "E", "F#", "G#"),
             "tensions": ("b9", "3", "b5", "#5", "7"),
             "order": 30},

            {"scale": "C# minor",
             "notes": ("C#", "E", "F#", "G#", "A"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 40},

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 50},

            {"scale": "G# minor 7b5",
             "notes": ("G#", "B", "C#", "D", "F#"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("A", "B", "C#", "F", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("A", "B", "D", "E", "F#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("A", "Bb", "C#", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("A", "C", "Eb", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
