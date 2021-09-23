# Umar's Maths stuff
Please report any bugs on [Github] 
(https://github.com/noneofyourbusiness1415252/Maths-stuff/issues) 

[Demonstration video] (https://www.loom.com/share/e7a3212ec2af446c81699a7f9109135f)

[Typewriter Effect] (https://www.loom.com/share/1096805bfb5d4819be558462933c6a5c)

Hello there and welcome to my Maths stuff!
This program currently identifies primes, composites, squares and cubes from within a range of number/s that you specify. It also includes quizzes about primes, squares and cubes.
To get started, just type a number from 1-7 to choose one of the options.   
All inputs must be written in integers (whole numbers). For the switching modes option, it allows you to switch modes if you type 'yes' in lowercase, uppercase or a mix, otherwise it continues on the same mode. For the typewriter effect speed, you can write any positive integer
## Primes/squares/cubes in range calculator
When finding squares/cubes/primes/composites in a certain range, the first number you will be asked for will be the **start** of the range, and the second number the **end** of the range, ***including itself***.
## Quiz  
For the square/cube quiz, type *square* if you think it is square, *cube* if you think it is cube, *both* if you think it is both square and cube, and *neither* if you think it is neither square nor cube.
## How questions are picked
The numbers picked quadratically increase depending on the level. There are theoretically infinite levels, but when the level gets really high the game becomes slower. *I won't be changing anyone's levels here!* ((-:)
### How the range of numbers is chosen
The formula to choose a number in each level is:
> `minimum = level ** 2 * 5 # level squared times five`

> `maximum = (level + 1) ** 2 * 5 # (level plus one) squared times five`

Examples:  
level 1 = 5 to 20  
level 2 = 20 to 45  
level 5 = 125 to 180  
level 10 = 500 to 605  
level 15 = 1125 to 1280  
level 20 = 2000 to 2205  
Woah, that escalated quickly, right?
### How each individual question is chosen
1. The range of numbers in the level are split equally into 5 groups.
2. If there are squares/cubes (if in square or cube quiz) or primes (if in prime quiz) in the first group, one of them is chosen at random.
3. Otherwise, any random number is chosen.
4. Step 2 or 3 repeated for the second, third, fourth and fifth group for the respective question
#### Example 1
Level: 5  
Range: 125 to 180  
Questions per group: 11  
Question groups are:  
1. 125 to 135  
2. 136 to 146  
3. 147 to 157  
4. 158 to 168  
5. 169 to 179  
Question 1 will be 125, because it is the only square/**cube** number in group 1.  
Question 2 will be 144, because it is the only **square**/cube number in group 2.  
Question 3 will be a random number from 147 to 157, because there are no squares or cubes in group 3.  
Question 4 will be any number from 158 to 168, for the same reason as question 3.   
Question 5 will be 169, for the same reason as question 2. 
#### Example 2
Level: 1  
Range: 5 to 20  
Questions per group: 3  
Question 1: 5, 6 or 7  
Question 2: 8 or 9, because they are both square or cube, but 10 isn't.  
Question 3: 10, 11 or 12  
Question 4: 13, 14 or 15  
Question 5: 16

## Typewriter Effect!
When choosing typewriter effect, the speed actually increases with a lower number because it is measured in ***average*** **seconds between each letter**.
So if you type in 0.1, 0.1 is multiplied by 2 to make 0.2, and the delay between each letter is a random number between 0 and 0.2 seconds. So it averages out to 0.1 seconds. 
The reason I made it like this instead of a fixed delay is so that it feels more natural, because you never type each letter with the exact same speed
## (Multi)Coloured text  
When you first use the program, you are asked if you want to turn on multicoloured text. Then it asks you to pick which colours you want in the text. The more times you type a colour, the more times it appears compared to the other colours. 
Example:
Cyan typed twice, red typed once, magenta typed thrice. Result: 1/2 of the text is magenta, 1/3 is cyan, 1/6 is red. 
# What I'm currently working on
I'm working on adding a discord bot with this program, as my friend Ammaar suggested.

Hope you like this tool! Have a good day!

  

