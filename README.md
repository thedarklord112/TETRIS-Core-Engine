# Tetris Logic Core Engine (Stateless Simulation)

=============================================================================================
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                            []                                             |
|                                          [][]                                             |
|                                          []                                               |
|                                                                    [][][]                 |
|                                                                      []                   |
|[]                                                                                         |
|[][]    []                                        [][][][]                                 |
|[][][][][]                                    [][][][][][][]                               |
|[][][][][][][][][][][]          [][][][][]    [][][][][][][][][][][]     []      [][][]    |
|[][][][]        [][][][][][][][][][][][][][][][][][][][][][][][][][][]  [][][][][][][][][][|
A production-grade, highly scalable, and object-oriented backend simulation engine that models the core gameplay mechanics of **Tetris**. Built entirely with clean **Python**, this repository focuses strictly on matrix transformation, 2D boundary collision parsing, and line-clear score routing without any heavy graphical overhead.

---

## 🚀 Key Features

- **In-Memory Matrix Rotations**: Implements clockwise 90-degree matrix transpositions using single-line Python slicing mechanisms (`zip(*matrix[::-1])`) to prevent rotation lag.
- **2D Boundary Collision Handler**: Real-time evaluation loop checking tetromino block indexes against left, right, bottom walls, and existing static grid structures.
- **Classic Scoring Pipeline**: Pre-configured scoring tier multipliers awarding bonus points dynamically for Single, Double, Triple, and maximum **Tetris (4 rows)** clear executions.
- **Stateless Physics Isolation**: Decouples game logic from rendering. You can easily plug this engine core into terminal screens, Pygame windows, web dashboards, or remote network protocols.

---

## 🎮 Code Architecture Overview

```text
├── src/
│   ├── __init__.py
│   ├── board.py         # 20x10 structural grid array, boundary collision & line-clearing
│   ├── tetromino.py     # Matrix definitions for the 7 geometric shapes & rotation logic
│   └── game.py          # Score pipelines, automated gravity ticks & game over evaluations
├── main.py              # CLI rendering entrypoint and keyboard action interceptor
└── README.md            # System documentation manual
```

---

## 🕹️ Quick Start & Execution

To test, control, and review the structural game execution blocks running live on your workstation, follow these rapid environment setup steps:

### 1. Download & Directory Routing
Extract your repository download zip folder package and navigate into the primary terminal directory:
```bash
# Enter the folder using the local path string
cd "C:\(\path\to\your\extracted\tetris-\)core-engine"
```

### 2. Launch the CLI Application
Run the primary execution script utilizing your system's python environment shell:
```bash
python main.py
```

---

## ⌨️ Controller Mapping

Once inside the interactive terminal match interface, input any action character command and strike **Enter** to step through the frame grid execution loop:

- **`a`** : Shifts the active tetromino piece one column to the **Left**
- **`d`** : Shifts the active tetromino piece one column to the **Right**
- **`w`** : Executes a clockwise **Rotation** matrix swap
- **`s`** : Triggers a gravity tick to **Drop** the piece down one single line
- **`q`** : **Quits** the engine loop and terminates the system process safely

---

## 🔒 Engine Security & Integration Guardrails
The logic core stores grid coordinates as safe, localized numerical integers (`0` for empty space, `1` for locked blocks, and `2` for moving structures). This clean state layout allows seamless integration with heavy multithreading pipelines or multiplayer streaming architectures.

## 📄 License
This open-source pack configuration is free for commercial or personal projects under the [MIT License](LICENSE).
