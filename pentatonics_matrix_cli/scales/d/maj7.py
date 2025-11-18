# maj7.py

SCALE_DATA = {
    "dmaj7": [
        {"notes": ("D", "F#", "A", "C#")},
        {"scales": [
            # --- Standard pentatonics ---
            {"scale": "b minor", 
             "notes": ("B", "D", "F#", "G", "A"),
             "tensions": ("13", "r", "3", "11", "5"), "order": 10},

            {"scale": "f# minor", 
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("3", "5", "13", "7", "9"), "order": 20},

            {"scale": "c# minor",
             "notes": ("C#", "E", "F#", "G#", "B"),
             "tensions": ("7", "9", "3", "#11", "13"), "order": 30},

            # --- Added pentatonics ---
            {"scale": "coltrane pentatonic",
             "notes": ("D", "E", "F#", "A#", "C"),
             "tensions": ("r", "9", "3", "#5", "7"), 
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("D", "E", "G", "A", "B"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("D", "Eb", "F#", "G#", "B"),
             "tensions": ("r", "b9", "3", "#11", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("D", "F", "G#", "B", "C"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},
        ]}
    ]
}
