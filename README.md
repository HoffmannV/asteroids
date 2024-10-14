
# Asteroids

Welcome to **Asteroids**, a Python-based game developed as part of the Boot.dev Back-End Developer Career Path. In this game, you control a spaceship and navigate through space while shooting asteroids. The game is built using the [Pygame](https://www.pygame.org/news) library.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [License](#license)

## Description

Asteroids is a simple 2D space shooter game where the player controls a spaceship that must avoid or destroy asteroids. The player can move the ship around the screen and fire projectiles to destroy asteroids. The objective is to survive and score points by destroying as many asteroids as possible.

This project is part of the Boot.dev Back-End Developer Career Path and was developed to practice Python skills and game development using the Pygame library.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/HoffmannV/asteroids.git 
    cd asteroids
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the game:

    ```bash
    python main.py
    ```

## How to Play

In **Asteroids**, your goal is to navigate your spaceship through an asteroid field while shooting down asteroids to avoid being hit. Each destroyed asteroid earns points. As the game progresses, the difficulty increases with more and faster asteroids appearing.

## Controls

- **W**: Move Up
- **A**: Rotate Left
- **S**: Move Down
- **D**: Rotate Right
- **Space**: Shoot projectiles

## Dependencies

- **Python 3.8+**
- **Pygame 2.6.0**
