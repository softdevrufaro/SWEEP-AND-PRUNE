# Sweep and Prune - Pygame Implementation

## About This Project

This project implements the **Sweep and Prune** collision detection algorithm in Python using the Pygame library. The Sweep and Prune algorithm is an efficient broad-phase collision detection technique commonly used in game engines and physics simulations.

## What is Sweep and Prune?

Sweep and Prune is a collision detection algorithm that works by:

1. **Sorting objects** along one or more axes (typically x, y, and z in 3D)
2. **Sweeping** through the sorted list to identify potentially overlapping pairs
3. **Pruning** pairs that clearly don't intersect, reducing the number of expensive detailed collision checks

This approach is particularly effective for scenarios with:
- Many static or slowly moving objects
- Objects spread across a large space
- Real-time performance requirements

## How It Works

### Algorithm Steps:

1. **Project all objects** onto the x and y axes as intervals
2. **Sort** the intervals on each axis
3. **Identify overlapping pairs** - only objects that overlap on ALL axes are potential collisions
4. **Perform detailed checks** on candidate pairs to determine actual collisions

### Advantages:

- **Efficient**: Reduces collision checks from O(n²) to approximately O(n) for well-distributed objects
- **Scalable**: Works well with a large number of objects
- **Simple**: Relatively straightforward to implement and understand

## Features

- Interactive Pygame visualization
- Real-time collision detection
- Visual representation of bounding boxes and collision pairs
- Configurable object count and movement

## Getting Started

### Requirements

- Python 3.x
- Pygame

### Installation

```bash
pip install pygame
```

### Running the Project

```bash
python main.py
```

## Project Structure

- `main.py` - Entry point for the application
- `sweep_and_prune.py` - Core algorithm implementation
- `objects.py` - Game object definitions and management
- `collision.py` - Collision detection and response logic

## Use Cases

- Game development for 2D collision detection
- Physics engine broad-phase testing
- Spatial partitioning in large game worlds
- Educational purposes for learning collision algorithms

## License

This project is open source and available for educational and development purposes.