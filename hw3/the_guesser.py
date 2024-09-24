import os, sys
from ezr import *



def branch(train):
    scoring_policies = [('exploit', lambda B, R,: B - R),
                        ('explore', lambda B, R :  (exp(B) + exp(R))/ (1E-30 + abs(exp(B) - exp(R))))]

    print(train,  flush=True, file=sys.stderr)
    print("\n"+train)
    repeats  = 20
    d        = DATA().adds(csv(train))
    b4       = [d.chebyshev(row) for row in d.rows]
    asIs,div = medianSd(b4)
    rnd      = lambda z: z

    print(f"asIs\t: {asIs:.3f}")
    print(f"div\t: {div:.3f}")
    print(f"rows\t: {len(d.rows)}")
    print(f"xcols\t: {len(d.cols.x)}")
    print(f"ycols\t: {len(d.cols.y)}\n")

    somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]

    for what,how in scoring_policies:
      for Last in [20, 30, 40, 50]:
        #print("The value of N is " + str(the.Last))
        N = Last
        for guesser in [True,False]:
          start = time()
          result = []
          runs = 0
          if guesser:
              guess_variable = "dumb"
          else:
              guess_variable = "smart"
          for _ in range(repeats):
            if guesser == True:
                #tmp is just guesses here no AL
                #dumb
                tmp = [guess_fn(d,N) for _ in range(20)][0]
                #print("fucked")
                #print(tmp[0][0])
                #tmp = [d.chebyshev( lst[0] ) for lst in tmp]
            else:
                #smart
                tmp=d.shuffle().activeLearning(score=how)
                #print(tmp[0])
                #tmp = [ d.chebyshev( lst[0] )for lst in tmp]
          runs += len(tmp)
          result += [rnd(d.chebyshev(tmp[0]))]

          pre=f"{guess_variable}/{Last}" if Last >0 else "guesser"
          tag = f"{pre},{int(runs/repeats)}"
          print(tag, f": {(time() - start) /repeats:.2f} secs")
          somes +=   [stats.SOME(result,    tag)]

    stats.report(somes, 0.01)
    
def guess_fn(d,N):
     some = random.choices(d.rows, k=N)
     #print(d.clone().adds(some).chebyshevs().rows[0])
     some_sorted = d.clone().adds(some).chebyshevs().rows
     return some_sorted

def main():
    train = sys.argv[1]
    if os.path.isfile(train):
        branch(train)
    else:
        print("Please enter a valid dataset")

main()
