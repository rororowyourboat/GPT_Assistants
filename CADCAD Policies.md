# CADCAD Policies

## Part 1: General Definitions

### Function: `vote_from_quorum_delegation`
- **Parameters**:
  - `user_quorum`: list of UserUUID
  - `project_id`: ProjectUUID
  - `action_matrix`: ActionMatrix
  - `user_decisions`: dict of UserUUID to Action
  - `params`: NQGModelParams
- **Returns**: Vote
- **Description**: Computes the quorum agreement for the active participants based on certain criteria.

### Function: `power_from_neural_governance`
- **Parameters**:
  - `uid`: UserUUID
  - `pid`: ProjectUUID
  - `neuron_layers`: list of NeuronLayer
  - `oracle_state`: OracleState
  - `initial_votes`: float (default: 0.0)
  - `print_on_each_layer`: bool (default: False)
- **Returns**: VotingPower
- **Description**: Computes a User Vote towards a Project using a Feedforward Neural Governance implementation.

## Part 2: Specific Definitions

### Function: `prior_voting_score`
- **Parameters**:
  - `user_id`: UserUUID
  - `oracle_state`: OracleState
- **Returns**: VotingPower
- **Description**: Oracle Module for the Prior Voting Score.

### Function: `reputation_score`
- **Parameters**:
  - `user_id`: UserUUID
  - `oracle_state`: OracleState
- **Returns**: VotingPower
- **Description**: Oracle Module for the Reputation Score.

### Function: `trust_score`
- **Parameters**:
  - `user_id`: UserUUID
  - `oracle_state`: OracleState
- **Returns**: VotingPower
- **Description**: Computes the Trust Score based on the Canonical Page Rank algorithm.

### Function: `LAYER_1_AGGREGATOR`
- **Description**: Aggregator function for Layer 1.

### Function: `LAYER_2_AGGREGATOR`
- **Description**: Aggregator function for Layer 2.

### Variables:
- `LAYER_1_NEURONS`: Dictionary of neurons for Layer 1.
- `LAYER_2_NEURONS`: Dictionary of neurons for Layer 2.
- `DEFAULT_NG_LAYERS`: List of default NeuronLayers.

This document provides an overview of CADCAD Policies implemented in the Python code provided.