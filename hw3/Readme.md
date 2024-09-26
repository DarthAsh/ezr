The experiment is run through an extension called the_guesser.py. To run this extension you simply need to run the command
python3.13 the_guesser.py path to your dataset

I have generated 2 bash files, guess_small.sh and guess_large.sh, which respectively run the extension for low and high dimensionality datasets.

guess_small.sh runs it for 7 low dimensionality datasets

guess_large.sh runs it for 4 medium and 3 large dimensionality datasets.

I have copied the results from rq.sh into an editor as they were not clearly readable in the command line.

For small dimensionality datasets
![Screenshot (93)](https://github.com/user-attachments/assets/e5fcd78b-d482-4b0f-89b1-ad012ac623ac)
For large dimensionality datasets
![Screenshot (94)](https://github.com/user-attachments/assets/7c526dbf-32ee-402a-8904-f23c0dd0c817)

In the above results: 

The 1st table tells us how often the treatments are in the ranks (0,1,2.....)

The 2nd table Evals is the budget used to achieve those ranks

The 3rd table Deltas is the precent difference of the current treatment with asIs when compared to asIs.


Results for small dimensionality datasets

For the smaller dimensionality datasets we can clearly see that the treatments smart/40 and smart/50 clearly get the best results for Ranking, Deltas as well as the budget Evaluation with smart/30 coming 2nd. smart/40 and smart50 are able to get their 1st ranks slightly more consistently than smart/30 gets it's 2nd. dumb/30 and dumb/50 are tied with smart/30 achieving rank 0 just as consistently. They are followed by smart/20, dumb/40 and dumb/20 in that order.

smart/40, smart/50 - Rank 0 - 71 times

smart/30, dumb/30, dumb/50 - Rank 0 - 57 times

smart/20,dumb/40 - rank 0 - 43 times

dumb/20 - rank 0 - 29 times


Conclusion for small dimensionality datasets

From the results we can conclude that 40,50 values guessed using the active learner gives us the best performance for small dimensionality datasets, while 30 and above randomly guessed values  and 20 values guessed with the active learner give us a fair amount of positive results. However 20 randomly guessed values gives us the worst performance.

Results for large/medium dimensionality datasets

For the large dimensionality datasets we can see that the treatments smart/20, smart/30 and smart/50 consistently give us the best results. smart/40 and dumb/40 also give us good results only slightly more inconsistently than the top rankers. dumb/30 and dumb/50 give us significantly worse results only achieving the top rank nearly half as many times as the x/40 treatments. dumb/20 consistently gives us rank 0 results the least number of times.

smart/30, smart/50, smart/20 - Rank 0 - 86 times

smart/40, dumb/40 - Rank 0 - 71 times

dumb/30, dumb/50 - Rank 0 - 43 times

dumb/20 - Rank 0 - 29 times


Conclusion for large/medium dimensionality results

From the results we can conclude that values guessed using the active learner give us the best performance for large dimensionality datasets. Randomly guessed values on the other hand consistently performed the worst(we will consider the dumb/40 treatment as an outlier).


Final Conclusion

We can hence refute the given hypothesis as results show that the active learner performs better than randomly guessed values for both small and large dimensionality datasets.
