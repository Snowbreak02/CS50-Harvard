# Snakes and Ladders Game for 2
#### Video Demo:  <URL HERE>
##### Description:

**The story and inspiration behind the code**
Unsure of what to even start on, I had to look and think back to the small and simple games that I used to enjoy as a kid. Snakes and Ladders is definetely one of the most famous board games that involves plenty of luck and very little thinking.

In this program, I strived to make the game as interactive and fun as possible, with different sorts of emojis as well as different comments and game inputs.

**What my project is**
As the name suggests, my code is based around a simple snakes and ladders game, with small twists. It is to be played by 2 players and in order to win, one player much ***reach the number 70*** and above before the other player does.

**How to play**
To start, read the welcome message. Enter both palyer's name and hit enter to start playing. In order to roll the dice, players must press enter. As the system will keep track of the movement of eachplayer, there is no need for the players to move themselves individually or remember their own numbers.

**The building blocks**
To start off, I had to determine the scope, whether I was to allow multiple unlimited players or just two. I was overwhelmed with the coding structure when I tried to take in multiple users, thus sticking to just 2 players in the end.

From the start, I had to define get_player_names() function to be able to ensure that player names do not match or contain any special characters. I personally didn't think it was necessary at first and just used a simple input for both names but I realised how ridiculous it was to have a text saying ~~'Mary' and 'Mary' will be playing against each other!⚔️~~

Next was combining functions within functions, where I had the get_dice_value() function and needing to to be combined with snake_ladder_actions(). It was a hassle as at firstI had inputted the format as snake_ladder_actions( dice_value, current_value, player_name), thus causing my dice_value to end up being my player_name value, resulting in the whole code breaking and me having to debugg it using the Run and Debug function. Thank god for it as I then found my mistake and was able to correct it.

Additionally, as I wanted it to be more intuitive and more exciting, I added in random texts for various actions, using the random.choice function. To add more of a retro old school game style to it and less program feel to it, I added a time.sleep(actions_delay) function. The actions_delay arguement was added later on as it was much easier to change this variable later on with just changing one number at the top instead of having to scroll through the whole code and change each number, making it more programmer friendly.

