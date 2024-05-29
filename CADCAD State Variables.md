# CADCAD State Variables

In the provided Python file, the CADCAD State Variables are defined within the context of a simulation model for Neural Quorum Governance (NQG). The state variables are used to represent the current state of the system being modeled and are crucial for simulating the dynamics of the system over time.

## OracleState Class
- **pagerank_results**: A dictionary mapping UserUUID to their pagerank value.
- **reputation_bonus_values**: A dictionary mapping UserUUID to their ReputationCategory.
- **prior_voting_bonus_values**: A dictionary mapping UserUUID to a list of prior voting bonus values.
- **reputation_bonus_map**: A dictionary mapping ReputationCategory to a float value.
- **prior_voting_bonus_map**: A dictionary mapping int (prior voting bonus index) to a float value.

## Vote Enum
- Represents the different voting actions a User can take towards a Project along with their corresponding Voting Power.
- Values: Yes (1.0), No (-1.0), Abstain (0.0).

## Action Enum
- Represents the decisions that a User can make in a Round.
- Values: RoundVote, Delegate, Abstain.

## User Class
- **label**: UserUUID.
- **reputation**: ReputationCategory of the user.
- **active_past_rounds**: Set of PastRoundIndex indicating the active past rounds for the user.

## NQGModelState TypedDict
- **days_passed**: Number of days passed.
- **delta_days**: Number of days for the time step.
- **users**: List of User objects.
- **user_round_decisions**: Dictionary mapping UserUUID to their Action in the current round.
- **delegatees**: DelegationGraph representing the delegation relationships.
- **trustees**: TrustGraph representing the trust relationships.
- **action_matrix**: Matrix mapping UserUUID to ProjectUUID to Vote.
- **vote_matrix**: Matrix mapping UserUUID to ProjectUUID to VotingPower.
- **per_project_voting**: Dictionary mapping ProjectUUID to VotingPower.
- **oracle_state**: OracleState object representing the state of the oracle.

## NQGModelParams TypedDict
- **label**: Label for the model.
- **timestep_in_days**: Time step duration in days.
- **quorum_agreement_weight_yes/no/abstain**: Weight for different quorum agreement types.
- **max_quorum_selected_delegates**: Maximum number of selected delegates for quorum.
- **max_quorum_candidate_delegates**: Maximum number of candidate delegates for quorum.
- **quorum_delegation_absolute_threshold**: Absolute threshold for quorum delegation.
- **quorum_delegation_relative_threshold**: Relative threshold for quorum delegation.
- **neuron_layers**: List of NeuronLayer objects.
- **initial_power**: Initial power value.
- **past_rounds**: Set of PastRoundIndex for neuron parameters.
- **projects**: Set of ProjectUUID representing the projects.
- **avg_new_users_per_day**: Average number of new users per day.
- **avg_user_past_votes**: Average number of past votes per user.
- **new_user_action_probability**: Probability of a new user taking action.
- **new_user_round_vote_probability**: Probability of a new user voting in a round.
- **new_user_project_vote_probability**: Probability of a new user voting on a project.
- **new_user_project_vote_yes_probability**: Probability of a new user voting 'Yes' on a project.
- **new_user_average_delegate_count**: Average number of delegates for a new user.
- **new_user_min_delegate_count**: Minimum number of delegates for a new user.
- **new_user_average_trustees**: Average number of trustees for a new user.

These state variables and parameters are essential for defining the initial state of the simulation model and for capturing the dynamics of the Neural Quorum Governance system over time.