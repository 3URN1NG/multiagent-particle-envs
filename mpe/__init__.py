from gym.envs.registration import register
import mpe.scenarios as scenarios
# Multiagent envs
# ----------------------------------------

_particles = {
    "multi_speaker_listener": "MultiSpeakerListener-v0",
    "simple_adversary": "SimpleAdversary-v0",
    "simple_crypto": "SimpleCrypto-v0",
    "simple_push": "SimplePush-v0",
    "simple_reference": "SimpleReference-v0",
    "simple_speaker_listener": "SimpleSpeakerListener-v0",
    "simple_spread": "SimpleSpread-v0",
    "simple_tag": "SimpleTag-v0",
    "simple_world_comm": "SimpleWorldComm-v0",
    "climbing_spread": "ClimbingSpread-v0",
}

for scenario_name, gymkey in _particles.items():
    scenario = scenarios.load(scenario_name + ".py").Scenario()
    world = scenario.make_world()

    # Registers multi-agent particle environments:
    register(
        gymkey,
        entry_point="mpe.environment:MultiAgentEnv",
        kwargs={
            "world": world,
            "reset_callback": scenario.reset_world,
            "reward_callback": scenario.reward,
            "observation_callback": scenario.observation,
        },
    )

for i in [3,4,5,6,7,8,9]:
    scenario = scenarios.load("simple_spread" + ".py").Scenario()
    world = scenario.make_world(cust_agents=i)

    # Registers multi-agent particle environments:
    register(
        "SimpleSpread-v0"+str(i),
        entry_point="mpe.environment:MultiAgentEnv",
        kwargs={
            "world": world,
            "reset_callback": scenario.reset_world,
            "reward_callback": scenario.reward,
            "observation_callback": scenario.observation,
        },
    )

# Registers the custom double spread environment:

for N in range(2, 11, 2):
    scenario_name = "simple_doublespread"
    gymkey = f"DoubleSpread-{N}ag-v0"
    scenario = scenarios.load(scenario_name + ".py").Scenario()
    world = scenario.make_world(N)

    register(
        gymkey,
        entry_point="mpe.environment:MultiAgentEnv",
        kwargs={
            "world": world,
            "reset_callback": scenario.reset_world,
            "reward_callback": scenario.reward,
            "observation_callback": scenario.observation,
        },
    )
