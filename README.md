## project-phase-3

# The Escapist

Collect tools, look for clues, and solve riddles in order to Escape your ultimate demise. (advanced deliverable: timed game)

Tools/Inventory

- C: Create tool when a new item gets picked up
- R: Show inventory of exisiting tool and new tool that you can choose to swap a slot for
- U: update the foreign key of the tool item so that it matches the owner
- D: delete an item from our inventory by it's id

Player/User

- C: Create new player/user
- R: Show welcome {player} name after user inputs their name
- D: Delete your player/user after they finish the game ("Do you want to delete yourself? GAME OVER")


# Object Relationships:

- one-to-one: Tools can only belong to one player
- one-to-many: A player can have multiple tools

# Constraints:

- player names: of type str and less than 15 characters
- tools: tools have to be of type Tool (instance)
  - tools name attribute should not be able to change


# User story map

![Untitled (1)](https://github.com/Idalisvaladez/Idalisvaladez/assets/139524475/8aad447c-53a3-4727-beca-b5ce96ddad64)


# Trello Board

![Untitled (2)](https://media.discordapp.net/attachments/1154791932111884351/1154858458412232745/image.png?width=1758&height=962)
