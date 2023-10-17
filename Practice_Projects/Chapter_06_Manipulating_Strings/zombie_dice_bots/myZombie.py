import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomDecisionZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        if zombiedice.roll() and random.choice([True, False]):
            zombiedice.roll()

class StopAfterTwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        while brains < 2:
            result = zombiedice.roll()
            if result is None:
                return
            brains += result['brains']

class StopAfterTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while shotguns < 2:
            result = zombiedice.roll()
            if result is None:
                return
            shotguns += result['shotgun']

class StopAfterTwoShotgunsOrMaxRollsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        max_rolls = random.randint(1, 4)
        shotguns = 0
        rolls = 0

        while shotguns < 2 or rolls < max_rolls:
            result = zombiedice.roll()
            if result is None:
                return
            shotguns += result['shotgun']
            rolls += 1

class StopAfterMoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()  # First roll

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()  # Roll again



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    RandomDecisionZombie(name='Random Decision'),  # Custom Zombie Bot 1
    StopAfterTwoBrainsZombie(name='Stop After 2 Brains'),  # Custom Zombie Bot 2
    StopAfterTwoShotgunsZombie(name='Stop After 2 Shotguns'),  # Custom Zombie Bot 3
    StopAfterTwoShotgunsOrMaxRollsZombie(name='Stop After 2 Shotguns or Max Rolls'),  # Custom Zombie Bot 4
    StopAfterMoreShotgunsThanBrainsZombie(name='Stop After More Shotguns Than Brains'),  # Custom Zombie Bot 5

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
