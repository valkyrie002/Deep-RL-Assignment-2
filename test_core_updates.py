"""Public tests for the standalone Part 1 exercises."""

import math
import unittest

from core_updates import discounted_returns, dqn_target, sarsa_target


class CoreUpdateTests(unittest.TestCase):
    def test_discounted_returns_assignment_example(self):
        actual = discounted_returns([1.0, 0.0, 2.0], 0.5)
        expected = [1.5, 1.0, 2.0]
        self.assertEqual(len(actual), len(expected))
        for got, want in zip(actual, expected):
            self.assertTrue(math.isclose(got, want, rel_tol=1e-9, abs_tol=1e-9))

    def test_discounted_returns_empty_episode(self):
        self.assertEqual(discounted_returns([], 0.9), [])

    def test_sarsa_nonterminal(self):
        self.assertTrue(math.isclose(sarsa_target(2.0, False, 4.0, 0.9), 5.6))

    def test_sarsa_terminal_does_not_bootstrap(self):
        self.assertTrue(math.isclose(sarsa_target(2.0, True, 999.0, 0.9), 2.0))

    def test_dqn_nonterminal_uses_largest_action_value(self):
        actual = dqn_target(2.0, False, [1.0, 4.0, 3.0], 0.9)
        self.assertTrue(math.isclose(actual, 5.6))

    def test_dqn_terminal_does_not_bootstrap(self):
        actual = dqn_target(2.0, True, [100.0, 400.0, 300.0], 0.9)
        self.assertTrue(math.isclose(actual, 2.0))


if __name__ == "__main__":
    unittest.main()
