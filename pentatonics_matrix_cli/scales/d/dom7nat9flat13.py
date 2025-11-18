# dom7nat9flat13.py

SCALE_DATA = {
    "d7nat9b13": [
        {"notes": ("D", "F#", "A", "C", "E", "Bb")},   # D–F#–A–C–E–Bb
        {"scales": [

            # --- Standard pentatonic ---
            {
                "scale": "f# whole tone",
                "notes": ("F#", "A#", "C", "D", "E"),
                "tensions": ("3", "b13", "b7", "r", "9"),
                "order": 10
            },

            # --- Added pentatonics ---
            {
                "scale": "coltrane pentatonic",
                "notes": ("D", "E", "F#", "A#", "C"),
                "tensions": ("r", "9", "3", "#5", "b7"),
                "order": 100
            },

            {
                "scale": "mccoy pentatonic",
                "notes": ("D", "E", "G", "A", "B"),
                "tensions": ("r", "9", "11", "5", "13"),
                "order": 110
            },

            {
                "scale": "hexatonic altered dominant pentatonic",
                "notes": ("D", "Eb", "F#", "G#", "B"),
                "tensions": ("r", "b9", "3", "#11", "13"),
                "order": 120
            },

            {
                "scale": "altered pentatonic",
                "notes": ("D", "F", "G#", "B", "C"),
                "tensions": ("r", "b3/#9", "b5", "13", "b7"),
                "order": 130
            },

        ]}
    ]
}
