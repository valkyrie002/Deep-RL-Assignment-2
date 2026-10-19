"""Standalone Part 1 exercises for CS 591 Project 2.

This file is intentionally independent of SLM-Lab.  Use only ordinary Python
numbers and lists; do not import NumPy or PyTorch.
"""


def discounted_returns(rewards, gamma):
    """Return a list containing G_0, G_1, ..., G_(T-1)."""
    outs = []
    discount = 1
    prev = 0
    for i in range (len(rewards)):
        current = rewards[len(rewards) - i - 1]
        outs.append(prev + current)
        prev = (prev + current) * gamma
    outs.reverse()
    return outs


def sarsa_target(reward, terminated, next_q_selected, gamma):
    """Return the scalar SARSA target for one transition."""
    if (terminated) :
        return reward
    return reward + (gamma * next_q_selected)


def dqn_target(reward, terminated, next_q_values, gamma):
    """Return the scalar DQN target for one transition."""
    if (terminated) :
        return reward
    return reward + (gamma * max(next_q_values))