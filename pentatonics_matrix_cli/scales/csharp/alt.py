# alt.py

SCALE_DATA = {
    "c#7alt": [
        {"notes": ("C#", "E#", "G", "G#", "B", "D", "Eb")},
        {"scales": [

            {"scale": "c# whole tone",
             "notes": ("C#", "E#", "Fx", "Gx", "Ax"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "a major b6",
             "notes": ("F", "A", "B", "C#", "E"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "e minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 30},

            {"scale": "d minor 6",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("b9", "3", "b5", "#5", "b7"),
             "order": 40},

            {"scale": "e minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "b minor 7b5",
             "notes": ("B", "D", "E", "F", "A"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C#", "D#", "E#", "Gx", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C#", "D#", "F#", "G#", "A#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C#", "D", "E#", "G", "A#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C#", "E", "G", "A#", "B"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
