# -*- coding: utf-8 -*-
"""RL-BlackJack.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v0RP8kj18CFlu8zKst0HQXhuYFE2A_3i
"""

import gymnasium as gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

class BlackJackQLearningAgent:
    def __init__(self, epsilon=0.2, alpha=0.2, gamma=0.99):
        """
        Initialize the Q-Learning agent for Blackjack.

        Args:
            epsilon (float): Exploration rate for epsilon-greedy policy.
            alpha (float): Learning rate for Q-Learning updates.
            gamma (float): Discount factor for future rewards.
        """
        self.env = gym.make('Blackjack-v1')

        self.epsilon = epsilon
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.99995
        self.alpha = alpha
        self.gamma = gamma

        self.Q = {}

    def get_state_key(self, state):
        """
        Convert the environment state to a key for the Q-table.

        Args:
            state (tuple): State representation from the environment.

        Returns:
            tuple: State key used for indexing the Q-table.
        """
        return tuple(state)

    def get_action(self, state):
        """
        Select an action using an epsilon-greedy policy.

        Args:
            state (tuple): Current state of the agent.

        Returns:
            int: Chosen action (0 for stick, 1 for hit).
        """
        state_key = self.get_state_key(state)
        player_sum, dealer_card, usable_ace = state

        if state_key not in self.Q:
            self.Q[state_key] = np.zeros(2)

        if np.random.random() < self.epsilon:
            return np.random.randint(2)
        else:
            return np.argmax(self.Q[state_key])

    def update(self, state, action, reward, next_state, done):
        """
        Update the Q-table based on the agent's experience.

        Args:
            state (tuple): Current state before taking the action.
            action (int): Action taken by the agent.
            reward (float): Reward received after taking the action.
            next_state (tuple): State after taking the action.
            done (bool): Whether the episode has ended.
        """
        state_key = self.get_state_key(state)

        if not done:
            next_state_key = self.get_state_key(next_state)
            if next_state_key not in self.Q:
                self.Q[next_state_key] = np.zeros(2)

            next_max = np.max(self.Q[next_state_key])
            self.Q[state_key][action] += self.alpha * (
                reward + self.gamma * next_max - self.Q[state_key][action]
            )
        else:
            self.Q[state_key][action] += self.alpha * (
                reward - self.Q[state_key][action]
            )

    def train(self, n_episodes=1000000):
        """
        Train the agent using Q-Learning over multiple episodes.

        Args:
            n_episodes (int): Number of episodes to train the agent.

        Returns:
            list: List of total rewards obtained in each episode.
        """
        rewards_history = []

        for episode in tqdm(range(n_episodes)):
            state, _ = self.env.reset()
            done = False
            total_reward = 0

            while not done:
                action = self.get_action(state)
                next_state, reward, done, truncated, _ = self.env.step(action)

                self.update(state, action, reward, next_state, done)
                total_reward += reward
                state = next_state

                if done or truncated:
                    break

            rewards_history.append(total_reward)

            # Decay epsilon
            self.epsilon = max(0.01, self.epsilon * 0.9999)

        return rewards_history

    def plot_training_results(self, rewards_history):
        """
        Plot the moving average of rewards obtained during training.

        Args:
            rewards_history (list): List of rewards obtained in each episode.
        """
        window_size = 1000
        moving_avg = pd.Series(rewards_history).rolling(window=window_size).mean()

        plt.figure(figsize=(10, 6))
        plt.plot(moving_avg)
        plt.title('Moving Average of Rewards During Training')
        plt.xlabel('Episode')
        plt.ylabel(f'Moving Average Rewards (window={window_size})')
        plt.grid(True)
        plt.show()

def evaluate_agent(agent, n_episodes=10000):
    """
    Evaluate the agent's performance over a specified number of episodes.

    Args:
        agent (BlackJackQLearningAgent): Trained Blackjack agent.
        n_episodes (int): Number of episodes to evaluate the agent.
    """
    wins = 0
    draws = 0
    losses = 0

    for _ in range(n_episodes):
        state, _ = agent.env.reset()
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, done, truncated, _ = agent.env.step(action)
            state = next_state

            if done or truncated:
                if reward > 0:
                    wins += 1
                elif reward == 0:
                    draws += 1
                else:
                    losses += 1
                break

    print(f"\nResults after {n_episodes} episodes:")
    print(f"Wins: {wins} ({wins/n_episodes*100:.1f}%)")
    print(f"Draws: {draws} ({draws/n_episodes*100:.1f}%)")
    print(f"Losses: {losses} ({losses/n_episodes*100:.1f}%)")

def watch_agent_play(agent, n_games=5, delay=2):
    """
    Visualize the agent playing Blackjack for a specified number of games.

    Args:
        agent (BlackJackQLearningAgent): Trained Blackjack agent.
        n_games (int): Number of games to watch.
        delay (int): Delay in seconds between actions for visualization.
    """
    import time

    for game in range(n_games):
        print(f"\n=== Game {game + 1} ===")
        state, _ = agent.env.reset()
        done = False

        while not done:
            # Display current state
            player_sum, dealer_card, has_ace = state
            print(f"\nYour card total: {player_sum}")
            print(f"Dealer's visible card: {dealer_card}")
            print(f"Usable ace: {'Yes' if has_ace else 'No'}")

            # Choose and execute action
            action = agent.get_action(state)
            print(f"Action chosen: {'Hit' if action == 1 else 'Stick'}")

            next_state, reward, done, truncated, info = agent.env.step(action)
            state = next_state

            time.sleep(delay)  # Pause for visualization

            if done:
                if reward > 0:
                    print("\n🎉 You won!")
                elif reward == 0:
                    print("\n🤝 It's a draw!")
                else:
                    print("\n😢 You lost!")
                print(f"Final reward: {reward}")
                time.sleep(delay)

# Instantiate and train the agent
agent = BlackJackQLearningAgent()
rewards_history = agent.train(n_episodes=1000000)
agent.plot_training_results(rewards_history)

# Evaluate the trained agent
evaluate_agent(agent)

# Watch the agent play
watch_agent_play(agent, n_games=5, delay=2)