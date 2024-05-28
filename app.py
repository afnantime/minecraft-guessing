import random
from fuzzywuzzy import fuzz

# Define a dictionary of block names and descriptions
blocks = {
    "diamond_block": {
        "hints": [
            "The hardest material found in Minecraft. It's shiny!",
            "It's the toughest block around, fit for a king's armor.",
            "This sparkly gem lights up the caves, but beware the pickaxe it takes.",
            "Used for tools that can break anything, this block is a miner's best friend.",
            "Deep underground, where lava flows, this precious treasure glows.",
            "Emerald lovers, rejoice! This block is what they truly voice."
        ]
    },
    "dirt": {
        "hints": [
            "The most common block. Great for planting things!",
            "The foundation of every build, from humble cottage to grand guild.",
            "Brown and basic, but essential still, for sprouting seeds and giving life its fill.",
            "Walk on it, build on it, or till its earthy soul, this block plays a vital role.",
            "From towering trees to vibrant flowers, this block holds nature's wondrous powers.",
            "Not as glamorous as diamond, but just as important for any farmer's command."
        ]
    },
    "cobblestone": {
        "hints": [ 
            "Made from breaking down stone. A reliable building block.",
            "Once common stone is broken and chipped,",
            "This rough and ready block leaves builders equipped.",
            "Strong and sturdy, it withstands the test,",
            "Of creeper blasts and zombie's quest.",
            "For castles grand or cozy homes, this block forever roams."
        ]
    },
    "redstone_block": {
        "hints": [
            "Powers amazing contraptions. Glows red!",
            "It pulses with a vibrant hue, bringing contraptions to life anew.",
            "Deeper than diamonds, this rock ignites, powering creations both day and night.",
            "Follow its trails, a hidden map, to wondrous gadgets that never nap.",
            "Redstone engineers, this is your prize, a spark of innovation that electrifies.",
            "Though it glows red, it holds no rage, just the potential to turn a new page."
        ]
    },
    "bookshelf": {
        "hints": [
            "Stores written knowledge. Can be crafted into lecterns.",
            "Words and wisdom fill its shelves, a library for every elf.",
            "Crafted from wood, its pages hold, stories whispered, both new and old.",
            "Librarians cherish its organized might, a beacon of knowledge, both day and night.",
            "Transform it with a lectern's touch, and share your wisdom, oh so much.",
            "Enchanting rooms embrace its lore, for powerful tools and so much more."
        ]
    },
    "netherrack": { 
        "hints": [
            "In the fiery depths where the Nether lies,",
            "This block burns eternal, a sight for sore eyes.",
            "Its crimson hue lights the dark,",
            "A blazing spark in a realm stark.",
            "Mined by the brave, this block of flame,",
            "A block found in the Nether. Burns forever!",
            "Is the heart of the Nether, its fiery claim."
        ]
    },
    "blue_ice": { 
        "hints": [
            "In icy realms where frost abounds,",
            "This block of blue, a slick ground.",
            "Slippery and smooth, a skater's dream,",
            "A chilly block by any stream.",
            "It never melts, it never tires,",
            "A slippery block that doesn't melt. Found in cold biomes.",
            "A frosty gem that never expires."
        ]
    },
    "soul_sand": {
        "hints": [
            "With every step, a slow descent,",
            "In the Nether's grasp, where souls cry,",
            "This sandy block makes you sigh.",
            "A haunting block, a dark lament.",
            "Souls swirl within its grim domain,",
            "A block that slows you down. Found in the Nether.",
            "A sandy trap, a realm of pain."
        ]
    },
    "end_stone": {
        "hints": [
            "In the void where shadows creep,",
            "This block of stone, a fortress keep.",
            "Enduring blasts and dragon's breath,",
            "A sturdy block that laughs at death.",
            "In the dragon's realm, where it's found,",
            "A block found in the End. Resistant to explosions.",
            "A block of strength, unyielding ground."
        ]
    },
    "glowstone": {
        "hints": [
            "This block shines without a care.",
            "In the Nether's glow, where light is rare,",
            "A beacon bright in the dark,",
            "A radiant gem, a fiery spark.",
            "Crafted by the brave, who dare to mine,",
            "A block that glows brightly. Found in the Nether.",
            "A block of light, a treasure divine."
        ]
    },
    "obsidian": {
        "hints": [
            "In the depths where lava flows,",
            "This block of black, a fortress grows.",
            "Hard as diamond, strong as steel,",
            "A miner's dream, a wizard's seal.",
            "Water meets lava, a hissing sound,",
            "A block that's hard to break. Created by pouring water on lava.",
            "Obsidian forms on solid ground."
        ]
    },
    "sea_pickle": {
        "hints": [
            "A block that emits light underwater. Found in warm oceans.",
            "In the ocean's depths, where corals sway,",
            "This pickle shines both night and day.",
            "A beacon bright beneath the sea,",
            "A glowing gem, a light so free.",
            "Warm oceans hold this treasure dear,",
            "A pickle's light, a sight so clear."
        ]
    },
    "sponge": {
        "hints": [
            "In the ocean's depths, where guardians roam,",
            "This block of sponge makes water its home.",
            "A thirsty block that drinks its fill,",
            "A sponge soaks up with a will.",
            "Ocean monuments guard this prize,",
            "A sponge that dries, a water-wise."
            "A block that soaks up water. Found in ocean monuments.",
        ]
    },
    "torch": {
        "hints": [
            "In the dark of night, where shadows loom,",
            "This block of light dispels the gloom.",
            "A torch to guide, a beacon bright,",
            "A flickering flame in the night.",
            "Monsters flee from its warm embrace,",
            "A torch's light, a safe space."
            "A block that emits light. Can be placed on walls.",
        ]
    },
    "concrete": {
        "hints": [
            "Solid color block. Crafted from concrete powder.",
            "Solid colors, bright and bold,",
            "A block that's crafted, strong and cold.",
            "Used in builds of modern style,",
            "It adds a touch that's versatile.",
            "Crafted from powder and water's mix, a concrete block is hard to fix."
        ]
    },
    "concrete_powder": {
        "hints": [
            "Falls like sand. Turns into concrete when it comes into contact with water.",
            "Soft and loose, it falls like sand,",
            "A block that shifts from hand to hand.",
            "Used in builds that change and flow,",
            "It turns to concrete with water's glow.",
            "Crafted from dye and gravel blend, a powder's journey finds its end."
        ]
    },
    "terracotta": {
        "hints": [
            "Colored clay block. Found in mesa biomes.",
            "Colored clay from mesa's ground,",
            "A block with hues that do astound.",
            "Used in builds both old and new,",
            "It adds a color that's tried and true.",
            "Found in biomes of red and gold, a terracotta's story is old."
        ]
    },
    "beehive": {
        "hints": [
            "Crafted home for bees. Can be harvested for honey.",
            "Crafted home for bees to thrive,",
            "A block where honey comes alive.",
            "Used to farm the honey pure,",
            "It keeps the bees and helps them cure.",
            "Crafted with planks and comb so neat, a beehive's work is truly sweet."
        ]
    },
    "bell": {
        "hints": [
            "Used to alert villagers of raids. Found in villages.",
            "Rings out loud with a clanging sound,",
            "A block that calls the villagers around.",
            "Used in villages to warn of fright,",
            "It rings the alarm both day and night.",
            "Crafted with gold and iron strong, a bell's ring is never wrong."
        ]
    },
    "campfire": {
        "hints": [
            "Cooks food and emits light. Found in villages.",
            "Warm and bright, it lights the night,",
            "A block for cooking, a camping delight.",
            "Used in villages and forest glades,",
            "It cooks your food and light pervades.",
            "Crafted from wood and coal combined, a campfire's glow is quite refined."
        ]
    },
    "scaffolding": {
        "hints": [
            "A block for builders, quick and light,",
            "A block that reaches to the skies.",
            "Temporary block for building. Can be climbed like ladders.",
            "Used to climb and build with ease,",
            "It's crafted from bamboo trees.",
            "Crafted with care, a scaffold's grace, a block that helps you reach the place."
        ]
    },
    "hay_bale": {
        "hints": [
            "Crafted from wheat. Often found in villages.",
            "Golden stack from farmer's yield,",
            "Used in stables, barns, and fields.",
            "Crafted from wheat, it's piled high,",
            "A sight that catches every eye.",
            "In villages, it stands so tall, a block that signifies a bountiful haul."
        ]
    },
    "lantern": {
        "hints": [
            "It shares the knowledge and dispels the glooms.",
            "A light that glows with a gentle hue,",
            "A block that shines both bright and true.",
            "Used in villages to light the way,",
            "It brightens the night and turns it to day.",
            "Crafted with iron and light so grand, a lantern's glow is quite in demand."
        ]
    },
     "blast_furnace": {
        "hints": [
            "Hot and quick, it smelts so fast,",
            "A furnace that roars with a blazing heat,",
            "A block that makes the ores complete.",
            "Used in villages to smelt with speed,",
            "It's crafted with iron, a builder's need.",
            "Crafted with care, a furnace's might, a block that makes your ores ignite."
        ]
     },
    "smoker": {
        "hints": [
            "Slow and steady, it cooks with care,",
            "A furnace that smokes with a gentle air,",
            "A block that cooks the food so rare.",
            "Used in villages to cook with grace,",
            "It's crafted with wood, a chef's embrace.",
            "Crafted with care, a smoker's delight, a block that cooks your food just right."
        ]
    },
        "beehive": {
            "hints": [
                "Crafted home for bees. Can be harvested for honey.",
                "Crafted home for bees to thrive,",
                "A block where honey comes alive.",
                "Used to farm the honey pure,",
                "It keeps the bees and helps them cure.",
                "Crafted with planks and comb so neat, a beehive's work is truly sweet."
            ]
        },
}


def check_guess(guess, block_name, threshold=80):
    # Convert to lowercase for case-insensitive matching
    guess = guess.lower()
    block_name = block_name.lower()

    # Use fuzz.ratio() for fuzzy matching score (0-100)
    score = fuzz.ratio(guess, block_name)

    # Check if score surpasses the threshold (adjustable)
    return score >= threshold

# Initialize score
score = 0

# Welcome message
print("Welcome to the Minecraft Block Guessing Game!")

while True:
    # Pick a random block
    random_block = random.choice(list(blocks.keys()))
    
    # Get the description for the chosen block
    hints = blocks[random_block]["hints"].copy()  # Use a copy to avoid modifying the original list

    # Ask the player to guess
    guess = input(f"What block am I thinking of? It {hints}.\n")

    # Check the guess with fuzzy matching (adjustable threshold)
    if check_guess(guess, random_block, threshold=80):
        score += 1
        print("Correct! You guessed the block.")
    else:
        # Offer a random hint
        while hints:
            hint = random.choice(hints)
            print(f"Hint: {hint}")
            hints.remove(hint)
            guess = input("Try again: ")
            if check_guess(guess, random_block, threshold=80):
                score += 1
                print("Correct! You guessed the block.")
                break
        if not hints:
            print(f"Incorrect. The block was {random_block}.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

# Thank the player for playing
print("Thanks for playing! Your final score is", score)
