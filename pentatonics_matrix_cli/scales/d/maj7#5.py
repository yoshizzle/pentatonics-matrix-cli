# maj7#5.py

SCALE_DATA = {
    "dmaj7#5": [
        {"notes": ("D", "F#", "A#", "C#")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "f# major b6",
                "notes": ("D", "F#", "G#", "A#", "C#"),
                "tensions": ("r", "3", "#11", "#5", "7"),
                "order": 10
            },

            {
                "scale": "c# minor 6",
                "notes": ("C#", "E", "F#", "G#", "A#"),
                "tensions": ("7", "9", "3", "#11", "#5"),
                "order": 20
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
                "tensions": ("r", "#9", "b5", "13", "b7"),
                "order": 130
            },

        ]}
    ]
}
