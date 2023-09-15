Original repository: https://github.com/asweigart/zombiedice  
The solution file could be better organized. The first bot works the same way as the `RandomCoinFlipZombie`, the third bot the same way as the `MinNumShotgunsThenStopZombie` with parameter `minShotguns = 2`.  
I would even say you could even change the code of the bot `MinNumShotgunsThenStopsZombie` to `MinNumBrainsThenStopsZombie` to create the second bot by just changing the variable to `brains`.  

Optimal bot strategy: https://www.researchgate.net/publication/262805512_Zombie_Dice_An_Optimal_Play_Strategy  
I recommend you checking YT videos in order to see how to play: 
* https://youtu.be/NMtlQxJeWvc?si=aZ8KMZkOZkN4cVXy
* https://youtu.be/ks44xnOadyM?si=k9mQ5Hg_kO_OqXaw

Check `examples.py` inside the subdirectory `src` in the original Al Sweigart repository in order to see the code behind his premade bots including the `MonteCarlo` one.  
⚠️ Yes, the last bot has that 0/1000 winning rate. This moderate-conservative strategy performs that bad in this press-to-luck game.   

Where to find the Deluxe physical Zombie Dice _board_ game: https://warehouse23.com/products/zombie-dice-deluxe-1?_pos=5&_sid=585f1cb32&_ss=r
