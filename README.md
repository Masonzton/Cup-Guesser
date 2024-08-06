Based on the tik tok trend where you try and guess the order of the cups.
https://www.tiktok.com/@klemfamily/video/7329231012624403758

play_game is for playing the game. Also tried out one strategy called the greedy strategy. This is choosing the guess that will result in the best worst case outcome at each step. After each guess, there will be a certain number of remaining permutations that are valid sequences. So working backwards from these candidate permutations, for each guess possible each of the candidate permutation will either have 0,1,2, or 4 correct digits. So the goal is to pick a guess such that each category is roughly equal. 
This strategy can always get the right sequence in 5 guesses. (But you will know the sequency after the 4th guess).

There might be a better strategy. But haven't been able to find it yet.
Interested to see how things are different for 6 cups instead of 4 cups. Also if you start adding extra rules.
Like you must move at least 3 cups for each guess. Another question is what the average or expected number of guesses are for a strategy and what the minimum number is.
Also maybe there is a strategy that is easier to remember and doesn't involve keeping track of exactly which combinations are left.