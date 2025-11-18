# maj7#11.py

SCALE_DATA = {
    "dmaj7#11": [
        {"notes": ("D", "F#", "A", "C#", "G#")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "b minor 6",
                "notes": ("B", "D", "E", "F#", "G#"),
                "tensions": ("13", "r", "9", "3", "#11"),
                "order": 10
            },

            {
                "scale": "c# minor",
                "notes": ("C#", "E", "F#", "G#", "B"),
                "tensions": ("7", "9", "3", "#11", "13"),
                "order": 20
            },

            {
                "scale": "g# whole tone",
                "notes": ("G#", "B#", "C##", "D#", "E#"),
                "tensions": ("#11", "7", "r", "9", "3"),
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
                "tensions": ("r", "#9", "b5", "13", "b7"),
                "order": 130
            },

        ]}
    ]
}
