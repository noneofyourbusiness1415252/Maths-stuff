# Umar's Maths stuff
![Maths: the only place where people buy 64 watermelons and no-one knows why...](https://www.bing.com/images/blob?bcid=RLGht7PssYcCsA "the truest meme ever")
Please report any bugs on [Github](https://github.com/noneofyourbusiness1415252/Maths-stuff/issues) 
[Demonstration video](https://www.loom.com/share/e7a3212ec2af446c81699a7f9109135f)
[Typewriter Effect](https://www.loom.com/share/1096805bfb5d4819be558462933c6a5c)
Hello there and welcome to my Maths stuff!
This program currently identifies primes, composites, squares and cubes from within a range of number/s that you specify. It also includes quizzes about primes, squares and cubes.
To get started, just type a number from 1-7 to choose one of the options.   
All inputs must be written in integers (whole numbers). For the switching modes option, it allows you to switch modes if you type 'yes' in lowercase, uppercase or a mix, otherwise it continues on the same mode. For the typewriter effect speed, you can write any positive integer
## Primes/squares/cubes in range calculator
When finding squares/cubes/primes/composites in a certain range, the first number you will be asked for will be the **start** of the range, and the second number the **end** of the range, ***including itself***.
## Quiz  
For the square/cube quiz, type *square* if you think it is square, *cube* if you think it is cube, *both* if you think it is both square and cube, and *no* if you think it is neither square nor cube.
## How questions are picked
The numbers picked quadratically increase depending on the level. There are theoretically infinite levels, but when the level gets really high the game becomes slower. If you really want to cheat your way to high levels, fork this program, click UserAccounts, then click your nickname, then click PrimeLevel or SquareOrCubeLevel depending on what you want to change, then change the number to what you want. *I won't be changing anyone's levels here!* ((-:)
### How the range of numbers is chosen
The formula to choose a number in each level is:
> maximum = level squared times ten
> minimum = maximum of previous level. 

There is an exception for level 1, because the formula above wouldn't work, so it is set manually to 1-10. Example question ranges include:
> level 1 = 1-10
level 2 = 10-40
level 5 = 160-250
level 10 = 810-1000
level 20 = 3610-4000
level 50 = 2401-2500
level 100 = 9801-10000
level 200 = 39601-40000
level 500 = 249001-250000

### How each individual question is chosen
1. Primes/squares and cubes respectively are counted within the range of numbers (which depends on level)
2. Each individual number is checked to see if it is prime/square or cube
3. The chance of that number getting picked is one divided by the amount of primes/composites or squares+cubes/not-square -or-cube numbers
#### Example 1
> Level: 2
Quiz: primes
Range: 10-40
8 Primes, 22 composites between 10-40
Number currently being checked: 17
17 is prime.
1 divided by 8 primes=12.5% chance of getting 17, or any other prime in level 2 range.

#### Example 2
> Level:3
Quiz:squares+cubes
Range:40-90
3 squares/cubes,47 other numbers between 10-40
Number currently being checked:47
47 is not square or cube.
1 divided by 47 non-square-or-cube numbers=about 2.13% chance of getting 47, or any other number that isn't square or cube in level 3 range.

## Typewriter Effect!
When choosing typewriter effect, the speed actually increases with a lower number because it is measured in ***average*** **seconds between each letter**.
So if you type in 0.1, 0.1 is multiplied by 2 to make 0.2, and the delay between each letter is a random number between 0 and 0.2 seconds. So it averages out to 0.1 seconds. 
The reason I made it like this instead of a fixed delay is so that it feels more natural, because you never type each letter with the exact same speed.
# What I'm currently working on
I'm working on adding a discord bot with this program, as my friend Ammaar suggested.

Hope you like this tool! Have a good day!

  

