# CADCAD State Update Blocks

## Introduction
In the context of CADCAD (Complex Adaptive Dynamics Computer-Aided Design), State Update Blocks are functions that define how the state of a system evolves over time in a simulation. These blocks are crucial in modeling the behavior of agents and entities within a system and capturing the dynamics of complex systems.

## Functions
1. **`generic_policy`**
    - Description: Function to generate a pass-through policy.
    - Arguments: `_1`, `_2`, `_3`, `_4`
    - Returns: Empty dictionary

2. **`replace_suf`**
    - Description: Creates a function for updating the state by replacing a variable with a new value.
    - Arguments: `variable (str)`, `default_value=0.0`
    - Returns: A function that continues the state across a substep

3. **`add_suf`**
    - Description: Creates a function for updating the state by adding a value to a variable.
    - Arguments: `variable (str)`, `default_value=0.0`
    - Returns: A function that continues the state across a substep

4. **`p_evolve_time`**
    - Description: Returns a signal for evolving time based on the timestep.
    - Arguments: `params: NQGModelParams`, `_2`, `_3`, `_4`
    - Returns: Signal with the delta days for the timestep

5. **`s_days_passed`**
    - Description: Updates the number of days passed in the state.
    - Arguments: `_1`, `_2`, `_3`, `state: NQGModelState`, `signal: Signal`
    - Returns: Variable update for the days passed

6. **`s_delta_days`**
    - Description: Updates the delta days in the state.
    - Arguments: `_1`, `_2`, `_3`, `_4`, `signal: Signal`
    - Returns: Variable update for the delta days

7. **`s_onboard_users`**
    - Description: Onboards new users with relevant properties through stochastic processes.
    - Arguments: `params: NQGModelParams`, `_2`, `_3`, `state: NQGModelState`, `_5`
    - Returns: Variable update for the users list

8. **`p_user_vote`**
    - Description: Makes new users decide on their actions (Abstain, Vote, or Delegate) using Bernoulli and Poisson processes.
    - Arguments: `params: NQGModelParams`, `_2`, `history: dict[int, dict[int, NQGModelState]]`, `state: NQGModelState`
    - Returns: Signal with updates for delegates, action matrix, and user round decisions

9. **`s_trust`**
    - Description: Makes new users trust each other by randomly sampling previous users.
    - Arguments: `params: NQGModelParams`, `_2`, `history`, `state: NQGModelState`, `_5`
    - Returns: Variable update for the trustees

10. **`s_oracle_state`**
    - Description: Updates the state of oracles (e.g., pagerank values and reputation weights).
    - Arguments: `params: NQGModelParams`, `_2`, `_3`, `state: NQGModelState`, `_5`
    - Returns: Variable update for the oracle state

11. **`p_compute_votes`**
    - Description: Performs Neural Quorum Governance to compute user votes based on actions and neural governance.
    - Arguments: `params: NQGModelParams`, `_2`, `_3`, `state: NQGModelState`
    - Returns: Signal with updates for vote matrix and per project voting

These functions collectively define the state update blocks for the CADCAD simulation, governing the evolution of the system state over time.