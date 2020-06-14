
# Introduction
This project is a recreation of the first world from Super Mario Bros on the NES using Pygame.
It was developed in the Pycharm IDE in two weeks. There are currently no plans to continue the project.

# Problems
A few problems that we encountered were:
* Drawing each tile with pygame is resource heavy
  * This causes in game lag if we have a large screen size
* Some hitboxes allow for interesting mechanics
  * Crouch jumping into a block and releasing the crouch can soft lock or teleport mario
  * Moving too fast can teleport mario through walls

# Tasks
- [ ] Fix lag when screen size is larger
- [ ] Fix physics
- [ ] Add enemies
- [ ] Fix Cheep Cheeps
- [ ] Add more levels
