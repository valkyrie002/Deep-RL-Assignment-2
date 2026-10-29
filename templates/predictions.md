# Project 2 Predictions and Reflection

Name: Valerie Barker

## Pre-run Predictions

Complete this section before viewing the corresponding final results. Do not
rewrite an original prediction later. If your thinking changes, explain why in
the Post-run Reflection section.

### REINFORCE learning rate

- Which learning rate do you expect to learn faster?
  - I expect a higher learning rate to learn faster. Since initially the parameter-space will be very un-optimized, it's likely larger steps in the direction of the gradient will yield greater initial improvement in loss.
- Which do you expect to be more stable across seeds?
  - I exect a lower learning rate to be more stable across seeds. A large learning rate has a large impact based on small changes in the parameter space, while a lower learning rate will be more stable as it doesn't take drastic measures based on the current gradient.
- Why?
  - A larger learning rate means taking larger steps in the direction of the gradient. The gradient can change depending on different initial weight values, and larger steps can cause greater divergence based on initial seeding. A smaller learning rate means smaller steps, which causes different seeds to take more similar paths.

### SARSA exploration

- Do you expect epsilon-greedy or Boltzmann selection to learn faster?
  - I expect Boltzmann selection to learn faster. Epsilon greedy uses random exploration based on the epsilon parameter. Boltzmann selection explores based on the probability distribution given by the Q function. Because of this, Boltzman selection allows a model to explore in a way that takes advantage of its current understanding and prioritize exploration of more promising choices.
- Do you expect the difference to persist late in training?
  - I think the difference will persist for complicated problems. If the problem complexity is high enough then it will be difficult for the model to fully learn the entire problem space. For this reason it becomes important to prioritize exploration of more promising prospects, and for this reason I believe Boltzman selection will be superior even late in training.
- Why?
  - Boltzman selection utilizes a probability distribution that takes advantage of the model's current understanding. If two choices seem similarly good (while other choices seem quite bad), Boltzman selection will help the model explore both of these candidates while epsilon greedy selection will congest the training with exploration of less attractive candidates.

### DQN exploration

- Do you expect epsilon-greedy or Boltzmann selection to learn faster?
  - I expect Boltzman selection to learn faster as it prioritizes exploration of more attractive candidates.
- Which do you expect to be more consistent across seeds?
  - I expect epsilon-greedy to be more consistent across seeds. Because boltzman selection determines its exploration based on the model's evaluation it's subject to variability based on the model's initial weight values. Epsilon greedy is independent of the model and therefore the initial weight values won't have that same impact.
- Why?
  - Boltzman selection encourages exploration based on the model's current understanding which allows the model to quickly investigate promising prospects. On the other hand for different initial weighting schemes this could cause a large variance because they could initially consider different choices promising and then upon further investigation have a cascading effect. It's like telling two different kids that they're good at math or english, and then as they invest more time into math and english because that's what they know leads to praise, they end up investing more and more into these fields and diverging in knowledge.

### DQN target-update frequency

- Complete this after Stage 3 selects the exploration rule but before launching
  the 1,000-update runs.
- Do you expect an update every 100 or every 1,000 training updates to learn
  faster?
  - I expect an update every 100 training updates to learn faster, since this allows it to make the most of new information in the learning process by updating the target network more frequently.
- Which do you expect to be more stable?
  - I expect an update every 1000 training updates to be more stable, since it doesn't immediately incorporate new information in the target network to generate loss, instead only updating the online network on stable target configurations.
- Why?
  - Updating more frequently allows the network to make use of its gained knowledge to learn faster with a more up to date target, but these updates are less stable since the updates to the target network are less reliable when we've done less training updates on the online network.

### Generalization

- Which DQN comparison will you transfer to Acrobot and Breakout?
- Do you expect the LunarLander ordering to hold in Acrobot? Why?
- Do you expect the LunarLander ordering to hold in Breakout? Why?

## Post-run Reflection

Preserve the predictions above. For each comparison, state what happened, what
surprised you, and how the evidence changed your explanation.
