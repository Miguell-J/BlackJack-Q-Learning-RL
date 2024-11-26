# 🃏 Blackjack Q-Learning Agent: Reinforcement Learning Mastery

<div align="center">
  
![image](https://github.com/user-attachments/assets/7d1987c1-08c3-4fff-9d30-31027b78ef69)
</div>

## 🌟 Project

An advanced implementation of reinforcement learning using the Q-Learning algorithm to solve the Gymnasium Blackjack environment, showcasing sophisticated machine learning techniques and adaptive decision-making strategies.

## 📊 Technical Overview

### Algorithm
- **Technique**: Q-Learning (Temporal Difference Learning)
- **Environment**: Gymnasium Blackjack-v1
- **Objective**: Develop an optimal strategy for playing Blackjack

### 🧠 Key Features
- Adaptive exploration via epsilon-greedy policy
- Dynamic Q-table updates
- Exponential exploration rate decay
- Robust handling of states and actions

## 🔬 Architectural Components

### `BlackJackQLearningAgent`
Core class encapsulating the complete reinforcement learning logic.

#### Hyperparameters
- `epsilon`: Initial exploration rate (0.2)
- `alpha`: Learning rate (0.2)
- `gamma`: Discount factor (0.99)

#### Key Methods
- `get_state_key()`: State conversion
- `get_action()`: Action selection
- `update()`: Policy update
- `train()`: Agent training

## 📈 Metrics and Analysis

### Performance Evaluation
- Training: 1,000,000 episodes
- Calculated metrics:
  - Win rate
  - Draw rate
  - Loss rate

### Visualization
- Moving average reward graph
- Learning progression over episodes

## 🚀 Dependencies

### Libraries Used
- `gymnasium`: Reinforcement learning environment
- `numpy`: Numerical computations
- `pandas`: Data manipulation
- `matplotlib`: Visualization
- `tqdm`: Training progress

## 💻 Installation & Execution

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
pip install gymnasium numpy pandas matplotlib tqdm
```

## 🧮 Mathematical Details

### Q-Learning Update Equation
Q(s,a) ← Q(s,a) + α * [R + γ * max(Q(s')) - Q(s,a)]

Where:
- Q(s,a): Action value
- α: Learning rate
- R: Reward
- γ: Discount factor
- max(Q(s')): Maximum Q-value for the next state

## 🔍 Implemented Strategies

### Exploration vs Exploitation
- **Epsilon-Greedy Policy**: Balances exploration and exploitation.
- **Exponential epsilon decay**: Gradual reduction in exploration over time.
- **Initial exploration vs progressive exploitation**: Prioritizes learning in early stages, optimizing decisions in later episodes.

### State Handling
- **Support for usable ace states**: Differentiates between hands with/without a usable ace.
- **Dynamic state-to-key mapping**: Ensures scalable and efficient state representation.

## 🎲 Demonstration

### Features
- **Agent Training**: Learn optimal strategies through extensive training sessions.
- **Result Plotting**: Visualize performance metrics and learning trends.
- **Performance Evaluation**: Assess win/loss/draw rates.
- **Game Visualization Mode**: Replay and observe trained agent decisions.

## 🔬 Complexity Analysis

### Space Complexity
- **O(n)**: The Q-table expands linearly with the number of unique states encountered.
- **Growth**: Directly proportional to the diversity of state-action pairs.

### Time Complexity
- **O(m * k)**: Training involves `m` episodes, each with an average of `k` steps.
- **Convergence**: Typically achieved after approximately 1,000,000 episodes, depending on hyperparameters.

## 🦾 Potential Extensions
- Implement **Deep Q-Learning** for enhanced scalability.
- Introduce **value function approximation** to generalize across state spaces.
- Experiment with **alternative reinforcement learning algorithms** (e.g., SARSA, Policy Gradient).
- Adapt and generalize the agent for **other casino-style games**.

## 📝 Contributions
Pull requests are welcome. For significant changes, open an issue first to discuss your ideas and proposed modifications.

## 📋 License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---
