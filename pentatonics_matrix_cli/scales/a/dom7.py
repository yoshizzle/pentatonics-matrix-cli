# dom7.py — A key center

SCALE_DATA = {
    "a7": [
        {"notes": ("A", "C#", "E", "G")},
        {"scales": [

            {"scale": "E minor 6",
             "notes": ("E", "G#", "A", "B", "C#"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "F# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "C# minor",
             "notes": ("C#", "E", "F#", "G#", "A"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "G# minor 7b5",
             "notes": ("G#", "B", "C#", "D", "F#"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "C minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "E major b2",
             "notes": ("E", "F", "G#", "B", "C#"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "G major b2",
             "notes": ("G", "A", "B", "D", "E"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "C# major b2",
             "notes": ("C#", "D", "E#", "G#", "A#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 80},

            {"scale": "F# major b2",
             "notes": ("F#", "G", "A#", "C#", "D#"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

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
