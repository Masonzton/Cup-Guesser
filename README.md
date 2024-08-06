Based on the tik tok trend where you try and guess the order of the cups.
https://www.tiktok.com/@klemfamily/video/7329231012624403758

play_game is for playing the game. Also tried out one strategy called the greedy strategy. This is choosing the guess that will result in the best worst case outcome at each step. After each guess, there will be a certain number of remaining permutations that could be the actual code. So working backwards from these candidate permutations, for each guess possible each of the candidate permutation will either have 0,1,2, or 4 correct digits. So the goal is to pick a guess such that each category is roughly equal. Specifically, the guess that will results in the smallest largest bin.

Testing the greedy strategy for 4,5,6 cups. It seems that the maximum number of guesses to know the sequence is equal to the number of cups. you can see the pictures of the histograms to see the distribution of results as well. Actually takes N+1 guesses since you need to do the last guess even if you already know the correct solution.

Things to look into: 

- There might be a better strategy and maybe one that is simpler / easier for a human to do. But haven't been able to find it yet.
- Does the pattern of requiring N guesses for N cups continue?
- Interested to see how things are different for adding extra rules. For example: you must move at least 3 cups for each guess.