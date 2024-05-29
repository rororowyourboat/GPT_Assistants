```markdown
# CADCAD Parameters

In the provided Python script, the CADCAD parameters for a Neural Quorum Governance (NQG) model are defined. These parameters are crucial for simulating the behavior of the governance system. Below are the key CADCAD parameters defined in the script:

1. **TIMESTEPS**: The total number of timesteps for the simulation is set to 100.
2. **SAMPLES**: The number of samples for the simulation is set to 1.

### Initial User and Project Parameters
3. **N_INITIAL_USERS**: Number of initial users in the system is set to 6.
4. **N_PROJECTS**: Number of projects in the system is set to 15.
5. **N_PAST_ROUNDS**: Number of past rounds considered in the simulation is set to 5.
6. **AVERAGE_PAST_VOTES_PER_USER**: Average past votes per user is set to 1.5.

### Default Project and Round Parameters
7. **PAST_ROUNDS**: Set of past rounds based on the number of past rounds defined.
8. **DEFAULT_PROJECTS**: Set of default projects named as 'proj_i' where i ranges from 0 to N_PROJECTS.

### Initial State Parameters
9. **INITIAL_ORACLE_STATE**: Initial state of the Oracle in the system with reputation and voting bonus maps.
10. **INITIAL_STATE**: Initial state of the NQG model with various attributes like days passed, users, decisions, delegates, trustees, etc.

### Single Run Parameters
11. **SINGLE_RUN_PARAMS**: Parameters for a single run of the NQG model including timestep, quorum weights, delegation thresholds, neural network layers, user actions, voting probabilities, and trustee counts.

These parameters play a significant role in defining the behavior and dynamics of the Neural Quorum Governance model within the CADCAD simulation framework.

```  