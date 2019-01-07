scales = {
    # C
    "CMaj7": [
        {"notes": ("C","E","G","B")},
        {"scales": [
            {"scale": "A minor", "notes":  ("A","C","E","F","G"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],
    "CMaj7#11": [
        {"notes": ("C","E","G","B","F#")},
        {"scales": [
            {"scale": "A minor 6", "notes": ("A","C","D","E","F#"), "tensions": ("13","R","9","3","#11"), "order": 10},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("7","9","3","#11","13"), "order": 20},
            {"scale": "F# Whole Tone", "notes": ("F#","A#","B#","D","E"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],
    "CMaj7#5": [
        {"notes": ("C","E","G#","B")},
        {"scales": [
            {"scale": "E Major b6", "notes": ("C","E","F#","G#","B"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "B minor 6", "notes": ("B","D","E","F#","G#"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],
    "CMaj7b5": [
        {"notes": ("C","E","Gb","B")},
        {"scales": [
            {"scale": "Gb minor 7b5", "notes": ("Gb","Bbb","Cb","Dbb","Fb"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],
    "Cmin7": [
        {"notes": ("C","Eb","G","Bb")},
        {"scales": [
            {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("R","b3","11","5","b7"), "order": 10},
            {"scale": "G minor", "notes": ("G","Bb","C","D","F"), "tensions": ("5","b7","R","9","11"), "order": 20},
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "Bb minor", "notes": ("Bb","Db","Eb","F","Ab"), "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],
    "Cmin6": [
        {"notes": ("C","Eb","G","A")},
        {"scales": [
            {"scale": "C minor 6", "notes": ("C","Eb","F","G","A"), "tensions": ("R","b3","11","5","13"),  "order": 10},
            {"scale": "A minor 7b5", "notes": ("A","C","D","Eb","G"), "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],
    "C7": [
        {"notes": ("C","E","G","Bb")},
        {"scales": [
            {"scale": "G minor 6", "notes": ("G","Bb","C","D","E"), "tensions": ("5","b7","R","9","3"), "order": 10},
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("9","11","5","13","R"), "order": 20},
            {"scale": "A minor", "notes": ("A","C","D","E","G"), "tensions": ("13","R","9","3","5"), "order": 30},
            {"scale": "E minor 7b5", "notes": ("E","G","A","Bb","D"), "tensions": ("3","5","13","b7","9"), "order": 40},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("#9","b5","#5","b7","b9"), "order": 50},
            {"scale": "C Major b2", "notes": ("C","Db","E","G","A"), "tensions": ("R","b9","3","5","13"), "order": 60},
            {"scale": "Eb Major b2", "notes": ("Eb","Fb","G","Bb","C"), "tensions": ("#9","3","5","b7","R"), "order": 70},
            {"scale": "F# Major b2", "notes": ("F#","G","A#","C#","D#"), "tensions": ("#11","5","b7","b9","#9"), "order": 80},
            {"scale": "A Major b2", "notes": ("A","Bb","C#","E","F#"), "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],
    "C7#11": [
        {"notes": ("C","E","G","Bb","F#")},
        {"scales": [
            {"scale": "G Whole Tone", "notes": ("G","Bb","C","D","E"), "tensions": ("5","b7","R","9","3"), "order":10},
            {"scale": "D Major b6", "notes": ("Bb","D","E","F#","G"), "tensions": ("b7","9","3","#11","5"), "order": 20},
            {"scale": "A minor 6", "notes": ("A","C","D","E","F#"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],
    "C7b9sus": [
        {"notes": ("C","F","G","Bb","Db")},
        {"scales": [
           {"scale": "Bb minor 6", "notes": ("Bb","Db","Eb","F","A"), "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],
    "C7nat9b13": [
        {"notes": ("C","E","G","Bb","D","Ab")},
        {"scales": [
           {"scale": "E Whole Tone", "notes": ("E","G#","A#","B#","D"), "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],
    "C7alt": [
        {"notes": ("C","E","Gb","G#","Bb","Db","D#")},
        {"scales": [
            {"scale": "C Whole Tone", "notes": ("C","E","F#","G#","A#"), "tensions": ("R","3","#11","#5","b7"), "order": 10},
            {"scale": "Ab Major b6", "notes": ("Fb","Ab","Bb","C","Eb"), "tensions": ("3","#5","b7","R","#9"), "order": 20},
            {"scale": "Db minor 6", "notes": ("Db","Fb","Gb","Ab","Bb"), "tensions": ("b9","3","b5","#5","7"), "order": 30},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("#9","b5","#5","b7","b9"), "order": 40},
            {"scale": "Eb minor 6", "notes": ("Eb","Gb","Ab","Bb","C"), "tensions": ("#9","b5","#5","b7","R"), "order": 50},
            {"scale": "Bb minor 7b5", "notes": ("Bb","Db","Eb","Fb","Ab"), "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
    "Cmin7b5": [
        {"notes": ("C","Eb","Gb","Bb")},
        {"scales": [
            {"scale": "Eb minor 6", "notes": ("Eb","Gb","Ab","Bb","C"), "tensions": ("b3","b5","13","b7","R"), "order": 10},
            {"scale": "C minor 7b5", "notes": ("C","Eb","F","Gb","Bb"), "tensions": ("R","b3","11","b5","b7"), "order": 20},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],
    "Cmin7b5nat9": [
        {"notes": ("C","Eb","Gb","Bb","D")},
        {"scales": [
           {"scale": "Bb Major b6", "notes": ("G","Bb","C","D","F"), "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],
    "Cmin/Maj7": [
        {"notes": ("C","Eb","G","B")},
        {"scales": [
            {"scale": "G Major b6", "notes": ("Eb","G","A","B","D"), "tensions": ("b3","5","13","7","9"),  "order": 10},
            {"scale": "B Whole Tone", "notes": ("B","Eb","F","G","A"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],
    # C#
    "C#Maj7": [
        {"notes": ("C#","E#","G#","B#")},
        {"scales": [
            {"scale": "A# minor", "notes":  ("A#","C#","E#","F#","G#"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "E# minor", "notes": ("E#","G#","A#","B#","D#"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "B# minor", "notes": ("B#","D#","E#","Fx","A#"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],
    "C#Maj7#11": [
        {"notes": ("C#","E#","G#","B#","Fx")},
        {"scales": [
            {"scale": "A# minor 6", "notes": ("A#","C#","D#","E#","Fx"), "tensions": ("13","R","9","3","#11"), "order": 10},
            {"scale": "B# minor", "notes": ("B#","D#","E#","Fx","A#"), "tensions": ("7","9","3","#11","13"), "order": 20},
            {"scale": "Fx Whole Tone", "notes": ("Fx","Ax","Bx","D#","E#"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],
    "C#Maj7#5": [
        {"notes": ("C#","E#","Gx","B#")},
        {"scales": [
            {"scale": "E# Major b6", "notes": ("C#","E#","Fx","Gx","B#"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "B# minor 6", "notes": ("B#","D#","E#","Fx","Gx"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],
    "C#Maj7b5": [
        {"notes": ("C#","E#","G","B#")},
        {"scales": [
            {"scale": "G minor 7b5", "notes": ("G","Bb","C","Db","F"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],
    "C#min7": [
        {"notes": ("C#","E","G#","B")},
        {"scales": [
            {"scale": "C# minor", "notes": ("C#","E","F#","G#","B"), "tensions": ("R","b3","11","5","b7"), "order": 10},
            {"scale": "G# minor", "notes": ("G#","B","C#","D#","F#"), "tensions": ("5","b7","R","9","11"), "order": 20},
            {"scale": "D# minor", "notes": ("D#","F#","G#","A#","C#"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("b7","b9","3","11","13"), "order": 40},
        ]},
    ],
    "C#min6": [
        {"notes": ("C#","E","G#","A#")},
        {"scales": [
            {"scale": "C# minor 6", "notes": ("C#","E","F#","G#","A#"), "tensions": ("R","b3","11","5","13"),  "order": 10},
            {"scale": "A# minor 7b5", "notes": ("A#","C#","D#","E","G#"), "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],
    "C#7": [
        {"notes": ("C#","E#","G#","B")},
        {"scales": [
            {"scale": "G# minor 6", "notes": ("G#","B","C#","D#","E#"), "tensions": ("5","b7","R","9","3"), "order": 10},
            {"scale": "A# minor", "notes": ("A#","C#","D#","E#","G#"), "tensions": ("13","R","9","3","5"), "order": 20},
            {"scale": "E# minor 7b5", "notes": ("E#","G#","A#","B","D#"), "tensions": ("3","5","13","b7","9"), "order": 30},
            {"scale": "C# Major b2", "notes": ("C#","D","E#","G#","A#"), "tensions": ("R","b9","3","5","13"), "order": 40},
            {"scale": "D# minor", "notes": ("D#","F#","G#","A#","C#"), "tensions": ("9","11","5","13","R"), "order": 50},
            {"scale": "E Major b2", "notes": ("E","F","G#","B","C#"), "tensions": ("#9","3","5","b7","R"), "order": 60},
            {"scale": "Fx Major b2", "notes": ("Fx","G#","Ax","Cx","Dx"), "tensions": ("#11","5","b7","b9","#9"), "order": 70},
            {"scale": "A# Major b2", "notes": ("A#","B","Cx","E#","Fx"), "tensions": ("13","b7","b9","3","#11"), "order": 80},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("#9","b5","#5","b7","b9"), "order": 90},
        ]},
    ],
    "C#7#11": [
        {"notes": ("C#","E#","G#","B","Fx")},
        {"scales": [
            {"scale": "G# Whole Tone", "notes": ("G#","B","C#","D#","E#"), "tensions": ("5","b7","R","9","3"), "order":10},
            {"scale": "D# Major b6", "notes": ("B","D#","E#","Fx","G#"), "tensions": ("b7","9","3","#11","5"), "order": 20},
            {"scale": "A# minor 6", "notes": ("A#","C#","D#","E#","Fx"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],
    "C#7b9sus": [
        {"notes": ("C#","F#","G#","B","D")},
        {"scales": [
           {"scale": "B minor 6", "notes": ("B","D","E","F#","A#"), "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],
    "C#7nat9b13": [
        {"notes": ("C#","E#","G#","B","D#","A")},
        {"scales": [
           {"scale": "E# Whole Tone", "notes": ("E#","Gx","Ax","Bx","D#"), "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],
    "C#7alt": [
        {"notes": ("C#","E#","G","Gx","B","D","Dx")},
        {"scales": [
            {"scale": "C# Whole Tone", "notes": ("C#","E#","Fx","Gx","Ax"), "tensions": ("R","3","#11","#5","b7"), "order": 10},
            {"scale": "A Major b6", "notes": ("F","A","B","C#","E"), "tensions": ("3","#5","b7","R","#9"), "order": 20},
            {"scale": "E minor 6", "notes": ("E","G","A","B","C#"), "tensions": ("#9","b5","#5","b7","R"), "order": 30},
            {"scale": "D minor 6", "notes": ("D","F","G","A","B"), "tensions": ("b9","3","b5","#5","b7"), "order": 40},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("#9","b5","#5","b7","b9"), "order": 50},
            {"scale": "B minor 7b5", "notes": ("B","D","E","F","A"), "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
    "C#min7b5": [
        {"notes": ("C#","E","G","B")},
        {"scales": [
            {"scale": "F# minor", "notes": ("F#","A","B","C#","E"), "tensions": ("11","13","b7","R","3"), "order": 10},
            {"scale": "E minor 6", "notes": ("E","G","A","B","C#"), "tensions": ("3","b5","13","b7","R"), "order": 20},
            {"scale": "C# minor 7b5", "notes": ("C#","E","F#","G","B"), "tensions": ("R","b3","11","5","b7"), "order": 30},
        ]},
    ],
    "C#min7b5nat9": [
        {"notes": ("C#","E","G","B","D#")},
        {"scales": [
           {"scale": "B Major b6", "notes": ("G#","B","C#","D#","F#"), "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],
    "C#min/Maj7": [
        {"notes": ("C#","E","G#","B#")},
        {"scales": [
            {"scale": "G# Major b6", "notes": ("E","G#","A#","B#","D#"), "tensions": ("3","5","13","7","9"),  "order": 10},
            {"scale": "B# Whole Tone", "notes": ("B#","E","F#","G#","A#"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],
    # iDb
    "DbMaj7": [
        {"notes": ("Db","F","Ab","C")},
        {"scales": [
            {"scale": "Bb minor", "notes":  ("Bb","Db","F","Gb","Ab"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],
    "DbMaj7#11": [
        {"notes": ("Db","F","Ab","C","G")},
        {"scales": [
           {"scale": "Bb minor 6", "notes": ("Bb","Db","Eb","F","G"), "tensions": ("13","R","9","3","#11"), "order": 10},
           {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("7","9","3","#11","13"), "order": 20},
           {"scale": "G Whole Tone", "notes": ("G","B","C","Eb","F"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],
    "DbMaj7#5": [
        {"notes": ("Db","F","A","C")},
        {"scales": [
            {"scale": "F Major b6", "notes": ("Db","F","G","A","C"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "C minor 6", "notes": ("C","Eb","F","G","A"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],
    "DbMaj7b5": [
        {"notes": ("Db","F","Abb","C")},
        {"scales": [
            {"scale": "Abb minor 7b5", "notes": ("Abb","Bb","C","Db","F"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],
    "Dbmin7": [
        {"notes": ("Db","Fb","Ab","Cb")},
        {"scales": [
            {"scale": "Db minor", "notes": ("Db","Fb","Gb","Ab","Cb"), "tensions": ("R","3","11","5","7"), "order": 10},
            {"scale": "Ab minor", "notes": ("Ab","Cb","Db","Eb","Gb"), "tensions": ("5","7","R","9","11"), "order": 20},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "Cb minor", "notes": ("Cb","Ebb","Fb","Gb","Bbb"), "tensions": ("7","b9","3","11","13"), "order": 40},
        ]},
    ],
    "Dbmin6": [
        {"notes": ("Db","Fb","Ab","Bb")},
        {"scales": [
            {"scale": "Db minor 6", "notes": ("Db","Fb","Gb","Ab","Bb"), "tensions": ("R","3","11","5","13"),  "order": 10},
            {"scale": "Bb minor 7b5", "notes": ("Bb","Db","Eb","Fb","Ab"), "tensions": ("13","R","9","3","5"), "order": 20},
        ]},
    ],
    "Db7": [
        {"notes": ("Db","F","Ab","Cb")},
        {"scales": [
            {"scale": "Ab minor 6", "notes": ("Ab","Cb","Db","Eb","F"), "tensions": ("5","7","R","9","3"), "order": 10},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("9","11","5","13","R"), "order": 20},
            {"scale": "Bb minor", "notes": ("Bb","Db","Eb","F","Ab"), "tensions": ("13","R","9","3","5"), "order": 30},
            {"scale": "F minor 7b5", "notes": ("F","Ab","Bb","Cb","Eb"), "tensions": ("3","5","13","7","9"), "order": 40},
            {"scale": "E minor", "notes": ("E","Abb","Bbb","Cb","Ebb"), "tensions": ("#9","b5","#5","7","b9"), "order": 50},
            {"scale": "Db Major b2", "notes": ("Db","Ebb","F","Ab","Bb"), "tensions": ("R","b9","3","5","13"), "order": 60},
            {"scale": "Fb Major b2", "notes": ("Fb","Gbb","Ab","Cb","Db"), "tensions": ("#9","3","5","7","R"), "order": 70},
            {"scale": "G Major b2", "notes": ("G","Ab","B","D","E"), "tensions": ("#11","5","7","b9","#9"), "order": 80},
            {"scale": "Bb Major b2", "notes": ("Bb","Cb","D","F","G"), "tensions": ("13","7","b9","3","#11"), "order": 90},
        ]},
    ],
    "Db7#11": [
        {"notes": ("Db","F","Ab","Cb","G")},
        {"scales": [
            {"scale": "Ab Whole Tone", "notes": ("Ab","Cb","Db","Eb","F"), "tensions": ("5","7","R","9","3"), "order":10},
            {"scale": "Eb Major b6", "notes": ("Cb","Eb","F","G","Ab"), "tensions": ("7","9","3","#11","5"), "order": 20},
            {"scale": "Bb minor 6", "notes": ("Bb","Db","Eb","F","G"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],
    "Db7b9sus": [
        {"notes": ("Db","Gb","Ab","Cb","Ebb")},
        {"scales": [
            {"scale": "Cb minor 6", "notes": ("Cb","Ebb","Fb","Gb","Bb"), "tensions": ("7","b9","#9","11","13"), "order": 20},
        ]},
    ],
    "Db7nat9b13": [
        {"notes": ("Db","F","Ab","Cb","Eb","Bbb")},
        {"scales": [
           {"scale": "F Whole Tone", "notes": ("F","A","B","C","Eb"), "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],
    "Db7alt": [
        {"notes": ("Db","F","Abb","A","Cb","Ebb","E")},
        {"scales": [
            {"scale": "Db Whole Tone", "notes": ("Db","F","G","A","B"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "Bbb Major b6", "notes": ("F","Bbb","Cb","Db","Fbb"), "tensions": ("3","#5","7","R","#9"), "order": 20},
            {"scale": "Ebb minor 6", "notes": ("Ebb","F","Abb","Bbb","Cb"), "tensions": ("b9","3","b5","#5","7"), "order": 30},
            {"scale": "Fb minor", "notes": ("Fb","Abb","Bbb","Cb","Ebb"), "tensions": ("#9","b5","#5","7","b9"), "order": 40},
            {"scale": "Fb minor 6", "notes": ("Fb","Abb","Bbb","Cb","Db"), "tensions": ("#9","b5","#5","7","R"), "order": 50},
            {"scale": "Cb minor 7b5", "notes": ("Cb","Ebb","Fb","F","Bbb"), "tensions": ("7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
    "Dbmin7b5": [
        {"notes": ("Db","Fb","Abb","Cb")},
        {"scales": [
            {"scale": "Fb minor 6", "notes": ("Fb","Abb","Bbb","Cb","Db"), "tensions": ("3","5","13","7","R"), "order": 10},
            {"scale": "Db minor 7b5", "notes": ("Db","Fb","Gb","Abb","Cb"), "tensions": ("R","3","11","5","7"), "order": 20},
            {"scale": "Gb minor", "notes": ("Gb","Bbb","Cb","Db","Fb"), "tensions": ("11","13","7","R","3"), "order": 30},
        ]},
    ],
    "Dbmin7b5nat9": [
        {"notes": ("Db","Fb","Abb","Cb","Eb")},
        {"scales": [
           {"scale": "Cb Major b6", "notes": ("Ab","Cb","Db","Eb","Gb"), "tensions": ("5","b7","R","9","11"), "order": 10},
        ]},
    ],
    "Dbmin/Maj7": [
        {"notes": ("Db","Fb","Ab","C")},
        {"scales": [
            {"scale": "Ab Major b6", "notes": ("Fb","Ab","Bb","C","Eb"), "tensions": ("3","5","13","7","9"),  "order": 10},
            {"scale": "Cb Whole Tone", "notes": ("Cb","Fb","Gb","Ab","Bb"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],
    # D
    "DMaj7": [
        {"notes": ("D","F#","A","C#")},
        {"scales": [
            {"scale": "B minor", "notes":  ("B","D","F#","G","A"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "F# minor", "notes": ("F#","A","B","C#","E"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "C# minor", "notes": ("C#","E","F#","G#","B"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],
    "DMaj7#11": [
        {"notes": ("D","F#","A","C#","G#")},
        {"scales": [
           {"scale": "B minor 6", "notes": ("B","D","E","F#","G#"), "tensions": ("13","R","9","3","#11"), "order": 10},
           {"scale": "C# minor", "notes": ("C#","E","F#","G#","B"), "tensions": ("7","9","3","#11","13"), "order": 20},
           {"scale": "G# Whole Tone", "notes": ("G#","B#","C#","E","F#"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],
    "DMaj7#5": [
        {"notes": ("D","F#","A#","C#")},
        {"scales": [
            {"scale": "F# Major b6", "notes": ("D","F#","G#","A#","C#"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "C# minor 6", "notes": ("C#","E","F#","G#","A#"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],
    "DMaj7b5": [
        {"notes": ("D","F#","Ab","C#")},
        {"scales": [
            {"scale": "Ab minor 7b5", "notes": ("Ab","B","C#","D","F#"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],
    "Dmin7": [
        {"notes": ("D","F","A","C")},
        {"scales": [
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("R","3","11","5","7"), "order": 10},
            {"scale": "A minor", "notes": ("A","C","D","E","G"), "tensions": ("5","7","R","9","11"), "order": 20},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("7","b9","3","11","13"), "order": 40},
        ]},
    ],
    "Dmin6": [
        {"notes": ("D","F","A","B")},
        {"scales": [
            {"scale": "D minor 6", "notes": ("D","F","G","A","B"), "tensions": ("R","3","11","5","13"),  "order": 10},
            {"scale": "B minor 7b5", "notes": ("B","D","E","F","A"), "tensions": ("13","R","9","3","5"), "order": 20},
        ]},
    ],
    "D7": [
        {"notes": ("D","F#","A","C")},
        {"scales": [
            {"scale": "A minor 6", "notes": ("A","C","D","E","F#"), "tensions": ("5","7","R","9","3"), "order": 10},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("9","11","5","13","R"), "order": 20},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("13","R","9","3","5"), "order": 30},
            {"scale": "F# minor 7b5", "notes": ("F#","A","B","C","E"), "tensions": ("3","5","13","7","9"), "order": 40},
            {"scale": "E# minor", "notes": ("E#","Ab","Bb","C","Eb"), "tensions": ("#9","b5","#5","7","b9"), "order": 50},
            {"scale": "D Major b2", "notes": ("D","Eb","F#","A","B"), "tensions": ("R","b9","3","5","13"), "order": 60},
            {"scale": "F Major b2", "notes": ("F","Gb","A","C","D"), "tensions": ("#9","3","5","7","R"), "order": 70},
            {"scale": "G# Major b2", "notes": ("G#","A","B#","D#","E#"), "tensions": ("#11","5","7","b9","#9"), "order": 80},
            {"scale": "B Major b2", "notes": ("B","C","D#","F#","G#"), "tensions": ("13","7","b9","3","#11"), "order": 90},
        ]},
    ],
    "D7#11": [
        {"notes": ("D","F#","A","C","G#")},
        {"scales": [
            {"scale": "A Whole Tone", "notes": ("A","C","D","E","F#"), "tensions": ("5","7","R","9","3"), "order":10},
            {"scale": "E Major b6", "notes": ("C","E","F#","G#","A"), "tensions": ("7","9","3","#11","5"), "order": 20},
            {"scale": "B minor 6", "notes": ("B","D","E","F#","G#"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],
    "D7b9sus": [
        {"notes": ("D","G","A","C","Eb")},
        {"scales": [
           {"scale": "C minor 6", "notes": ("C","Eb","F","G","B"), "tensions": ("7","b9","#9","11","13"), "order": 20},
        ]},
    ],
    "D7nat9b13": [
        {"notes": ("D","F#","A","C","E","Bb")},
        {"scales": [
           {"scale": "F# Whole Tone", "notes": ("F#","A#","B#","C#","E"), "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],
    "D7alt": [
        {"notes": ("D","F#","Ab","A#","C","Eb","E#")},
        {"scales": [
            {"scale": "D Whole Tone", "notes": ("D","F#","G#","A#","B#"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "Bb Major b6", "notes": ("F#","Bb","C","D","Fb"), "tensions": ("3","#5","7","R","#9"), "order": 20},
            {"scale": "Eb minor 6", "notes": ("Eb","F#","Ab","Bb","C"), "tensions": ("b9","3","b5","#5","7"), "order": 30},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("#9","b5","#5","7","b9"), "order": 40},
            {"scale": "F minor 6", "notes": ("F","Ab","Bb","C","D"), "tensions": ("#9","b5","#5","7","R"), "order": 50},
            {"scale": "C minor 7b5", "notes": ("C","Eb","F","F#","Bb"), "tensions": ("7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
    "Dmin7b5": [
        {"notes": ("D","F","Ab","C")},
        {"scales": [
            {"scale": "F minor 6", "notes": ("F","Ab","Bb","C","D"), "tensions": ("3","5","13","7","R"), "order": 10},
            {"scale": "D minor 7b5", "notes": ("D","F","G","Ab","C"), "tensions": ("R","3","11","5","7"), "order": 20},
            {"scale": "G minor", "notes": ("G","Bb","C","D","F"), "tensions": ("11","13","7","R","3"), "order": 30},
        ]},
    ],
    "Dmin7b5nat9": [
        {"notes": ("D","F","Ab","C","E")},
        {"scales": [
           {"scale": "C Major b6", "notes": ("A","C","D","E","G"), "tensions": ("5","b7","R","9","11"), "order": 10},
        ]},
    ],
    "Dmin/Maj7": [
        {"notes": ("D","F","A","C#")},
        {"scales": [
            {"scale": "A Major b6", "notes": ("F","A","B","C#","E"), "tensions": ("3","5","13","7","9"),  "order": 10},
            {"scale": "C Whole Tone", "notes": ("C#","F","G","A","B"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],
    # Eb
    "EbMaj7": [
        {"notes": ("Eb","G","Bb","D")},
        {"scales": [
            {"scale": "C minor", "notes":  ("C","Eb","G","Ab","Bb"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "G minor", "notes": ("G","Bb","C","D","F"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],
    "EbMaj7#11": [
        {"notes": ("Eb","G","Bb","D","A")},
        {"scales": [
           {"scale": "C minor 6", "notes": ("C","Eb","F","G","Ab"), "tensions": ("13","R","9","3","#11"), "order": 10},
           {"scale": "D minor", "notes": ("D","F","G","Ab","C"), "tensions": ("7","9","3","#11","13"), "order": 20},
           {"scale": "A Whole Tone", "notes": ("A","D","Eb","F","G"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],
    "EbMaj7#5": [
        {"notes": ("Eb","G","B","D")},
        {"scales": [
            {"scale": "G Major b6", "notes": ("Eb","G","A","B","D"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "D minor 6", "notes": ("D","F","G","A","B"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],
    "EbMaj7b5": [
        {"notes": ("Eb","G","Bb","D")},
        {"scales": [
            {"scale": "A minor 7b5", "notes": ("A","C","D","Eb","G"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],
    "Ebmin7": [
        {"notes": ("Eb","Gb","Bb","Db")},
        {"scales": [
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("R","b3","11","5","b7"), "order": 10},
            {"scale": "Bb minor", "notes": ("Bb","Db","Eb","F","Ab"), "tensions": ("5","b7","R","9","11"), "order": 20},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "Db minor", "notes": ("Db","E","Gb","Ab","C"), "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],
    "Ebmin6": [
        {"notes": ("Eb","Gb","Bb","C")},
        {"scales": [
            {"scale": "Eb minor 6", "notes": ("Eb","Gb","Ab","Bb","C"), "tensions": ("R","b3","11","5","13"),  "order": 10},
            {"scale": "C minor 7b5", "notes": ("C","Eb","F","Gb","Bb"), "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],
    "Eb7": [
        {"notes": ("Eb","G","Bb","Db")},
        {"scales": [
            {"scale": "Bb minor 6", "notes": ("Bb","Db","Eb","F","G"), "tensions": ("5","b7","R","9","3"), "order": 10},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("9","11","5","13","R"), "order": 20},
            {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("13","R","9","3","5"), "order": 30},
            {"scale": "G minor 7b5", "notes": ("G","Bb","C","Db","F"), "tensions": ("3","5","13","b7","9"), "order": 40},
            {"scale": "F# minor", "notes": ("F#","A","B","Db","Fb"), "tensions": ("#9","b5","#5","b7","b9"), "order": 50},
            {"scale": "Eb Major b2", "notes": ("Eb","Fb","G","Bb","C"), "tensions": ("R","b9","3","5","13"), "order": 60},
            {"scale": "Gb Major b2", "notes": ("Gb","G","Bb","Db","Eb"), "tensions": ("#9","3","5","b7","R"), "order": 70},
            {"scale": "A Major b2", "notes": ("A","Bb","Db","Fb","F#"), "tensions": ("#11","5","b7","b9","#9"), "order": 80},
            {"scale": "C Major b2", "notes": ("C","Db","Fb","G","A"), "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],
    "Eb7#11": [
        {"notes": ("Eb","G","Bb","Db","A")},
        {"scales": [
            {"scale": "Bb Whole Tone", "notes": ("Bb","Db","Eb","F","G"), "tensions": ("5","b7","R","9","3"), "order":10},
            {"scale": "F Major b6", "notes": ("Db","F","G","A","Bb"), "tensions": ("b7","9","3","#11","5"), "order": 20},
            {"scale": "C minor 6", "notes": ("C","Eb","F","G","A"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],
    "Eb7b9sus": [
        {"notes": ("Eb","Ab","Bb","Db","Fb")},
        {"scales": [
           {"scale": "Db minor 6", "notes": ("Db","Fb","F#","Ab","C"), "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],
    "Eb7nat9b13": [
        {"notes": ("Eb","G","Bb","Db","F","Cb")},
        {"scales": [
           {"scale": "G Whole Tone", "notes": ("G","Bb","Db","Eb","F"), "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],
    "Eb7alt": [
        {"notes": ("Eb","G","A","Bb","Db","Fb","F#")},
        {"scales": [
            {"scale": "Eb Whole Tone", "notes": ("Eb","G","A","B","Db"), "tensions": ("R","b3","#11","#5","b7"), "order": 10},
            {"scale": "B Major b6", "notes": ("G","B","Db","Eb","F#"), "tensions": ("b3","#5","b7","R","#9"), "order": 20},
            {"scale": "Fb minor 6", "notes": ("Fb","G","Bbb","B","Db"), "tensions": ("b9","b3","b5","#5","b7"), "order": 30},
            {"scale": "F# minor", "notes": ("F#","Bbb","B","Db","Fb"), "tensions": ("#9","b5","#5","b7","b9"), "order": 40},
            {"scale": "F# minor 6", "notes": ("F#","Bbb","B","Db","Eb"), "tensions": ("#9","b5","#5","b7","R"), "order": 50},
            {"scale": "Db minor 7b5", "notes": ("Db","Fb","F#","Bbb","B"), "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
    "Ebmin7b5": [
        {"notes": ("Eb","Gb","Bbb","Db")},
        {"scales": [
            {"scale": "Gb minor 6", "notes": ("Gb","Bb","C","Db","Eb"), "tensions": ("b3","5","13","b7","R"), "order": 10},
            {"scale": "Eb minor 7b5", "notes": ("Eb","Gb","Ab","Bbb","Db"), "tensions": ("R","b3","11","b5","b7"), "order": 20},
            {"scale": "Ab minor", "notes": ("Ab","Cb","Db","Eb","Gb"), "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],
    "Ebmin7b5nat9": [
        {"notes": ("Eb","Gb","Bbb","Db","F")},
        {"scales": [
           {"scale": "C Major b6", "notes": ("Bb","Db","Eb","F","Ab"), "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],
    "Ebmin/Maj7": [
        {"notes": ("Eb","G","Bb","D")},
        {"scales": [
            {"scale": "Bb Major b6", "notes": ("G","Bb","C","D","F"), "tensions": ("b3","5","13","7","9"),  "order": 10},
            {"scale": "D Whole Tone", "notes": ("D","Gb","Ab","Bb","C"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ]
}
