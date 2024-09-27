The experiment is run through an extension called the_guesser.py. To run this extension you simply need to run the command
python3.13 the_guesser.py path to your dataset

I have generated 2 bash files, guess_small.sh and guess_large.sh, which respectively run the extension for low and high dimensionality datasets.

To run the experiment simply run these bash files. You will have to create the tmp and tmp2 directories.

guess_small.sh runs it for 7 low dimensionality datasets

guess_large.sh runs it for 4 medium and 3 large dimensionality datasets.

I have copied the results from rq.sh into an editor as they were not clearly readable in the command line.

For small dimensionality datasets
![Screenshot (95)](https://github.com/user-attachments/assets/e4910212-a571-4010-adec-cc69600db006)

For large dimensionality datasets
![Screenshot (96)](https://github.com/user-attachments/assets/4856975a-7674-48c4-9adb-2bc847829506)

In the above results: 

The 1st table tells us how often the treatments are in the ranks (0,1,2.....)

The 2nd table Evals is the budget used to achieve those ranks

The 3rd table Deltas is the precent difference of the current treatment with asIs when compared to asIs.

smart - uses active learner, dumb - randomly picked

Results for small dimensionality datasets

For the smaller dimensionality datasets we can clearly see that the treatments smart/40 and dumb/50 clearly get the best results for 0 rank consistently. Followed closely by dumb/40. smart/50 and smart/20 both performed equally well with dumb/30 anddumb/20 giving the worst results.

smart/40, dumb/50 - Rank 0 - 86 times

dumb/40 - Rank 0 - 71 times

smart/50,smart/20 - rank 0 - 57 times

dumb/30 - rank 0 - 29 times

dumb/20 - rank 0 - 14

Results for large/medium dimensionality datasets

For the large dimensionality datasets we can see that the treatment dumb/40 gave the best result every time it was run. It was followed by smart/20, smart/30 and dumb/50 which all performed equally well and only silghtly worse than the dumb/40. smart/50 and smart/40 performed decently but significantly worse than dumb/40. dumb/20  and dumb/30 consistently gaves us rank 0 results the least number of times.

dumb/40 - Rank 0 - 100 times

smart/30, smart/20, dumb/50  - Rank 0 - 86 times

smart/40, smart/50 - Rank 0 - 71 times

dumb/30, dumb/20 - Rank 0 - 29 times


Conclusion for large/medium dimensionality results


Final Conclusion

From these results we can conclude that for small dimensionality datasets using active learners more or less gives us the same result as using randomly picked values and surpisingly the same goes for 
large dimensionality datasets. Thus the given hypothese has been proven true for these particular 7 small and 7 large dimnesionality datasets.



ps: I didnt write test cases as all the code used is from ezr or from python libraries(also didnt get ime because of midterms :( ). Pls advice on how to write them and I shall resubmit.Thanks!!
