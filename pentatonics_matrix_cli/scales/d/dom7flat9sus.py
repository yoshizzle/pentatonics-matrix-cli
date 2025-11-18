# dom7flat9sus.py

SCALE_DATA = {
    "d7b9sus": [
        {"notes": ("D", "G", "A", "C", "Eb")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "c minor 6",
                "notes": ("C", "Eb", "F", "G", "A"),
                "tensions": ("b7", "b9", "#9", "11", "13"),
                "order": 10
            },

            # (C7b9sus had only one standard entry, so we match the structure)
            # No 20-order standard scale in the C model → remain consistent.

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
