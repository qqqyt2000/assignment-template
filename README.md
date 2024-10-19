# QiuYuting_Assignment3_Penguin and Pizza
QiuYuting_24047199G_SD5913 - Assignment template

## Brief
* I used PyGame to create a two-player game, in which two little penguins compete for a slice of pizza that appears randomly on the screen.
* Run the main program "penguin and pizza.py", and the game interface will appear. Click the yellow part to view the rule file, and click the play button to start.
* Because the game involves multiple control buttons and objects, I encapsulated them in different programs using Class to facilitate the calling of the main program.
* Here are the rules of the game:

## Rules
**Controls** 
* Use ↑←↓→ to control the bottom right penguin (Penguin ONE). Its scoreboard is located at the top right.
* Use WASD to control the bottom left penguin (Penguin TWO). Its scoreboard is located at the top left.
* Click the Play button with the left mouse button to start the game.
* Click the Records button with the left mouse button to view past game records.
* After reaching the specified goal, the game will return to the initial screen. Click the Play button with the left mouse button to start a new round.

**Game Rules**
* Once the game starts, both players control their penguins to compete for a pizza that appears randomly on the screen. If a penguin's center point is within the pizza image, that player scores a point.
* The pizza changes position every two seconds.
* If a player grabs the pizza within two seconds, the next pizza appears immediately.
* When a total of ten pizzas have been grabbed (i.e., the combined score of both players is 10), the game ends. The player with the higher score wins. If the scores are tied, the game is a draw.
