# min7b5nat9.py

SCALE_DATA = {
    "dmin7b5nat9": [
        {"notes": ("D", "F", "G#", "C", "E")},   # D – F – Ab – C – E
        {"scales": [

            # --- Standard pentatonic (parallel Major b6 model) ---
            {
                "scale": "c major b6",
                "notes": ("A", "C", "D", "E", "G"),
                "tensions": ("b5", "b7", "r", "9", "11"),
                "order": 10
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
