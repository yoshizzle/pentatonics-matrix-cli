# min7flat5nat9.py

SCALE_DATA = {
    "cmin7b5nat9": [
        {"notes": ("C", "Eb", "Gb", "Bb", "D")},
        {"scales": [
            {"scale": "bb major b6", "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("b5", "b7", "r", "9", "11"), "order": 10},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "Gb", "A"),
             "tensions": ("r", "9", "b3", "b5", "13"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "Gb", "Bb"),
             "tensions": ("r", "9", "11", "b5", "b7"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "Eb", "Gb", "A"),
             "tensions": ("r", "b9", "b3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "b3", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
