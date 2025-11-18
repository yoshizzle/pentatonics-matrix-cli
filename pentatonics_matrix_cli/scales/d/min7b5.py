# min7b5.py

SCALE_DATA = {
    "dmin7b5": [
        {"notes": ("D", "F", "G#", "C")},   # D – F – Ab – C
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "f minor 6",
                "notes": ("F", "G#", "Bb", "C", "D"),
                "tensions": ("b3", "b5", "13", "b7", "r"),
                "order": 10
            },

            {
                "scale": "d minor 7b5",
                "notes": ("D", "F", "G", "G#", "C"),
                "tensions": ("r", "b3", "11", "b5", "b7"),
                "order": 20
            },

            {
                "scale": "g minor",
                "notes": ("G", "Bb", "C", "D", "F"),
                "tensions": ("11", "b13", "b7", "r", "b3"),
                "order": 30
            },

            # --- Added pentatonics ---
            {
                "scale": "coltrane pentatonic",
                "notes": ("D", "E", "F#", "A#", "C"),
                "tensions": ("r", "9", "3", "#5", "7"),
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
