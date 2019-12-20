import numpy as np

#-----------------------------------------------------------------------------------------
#    Algorithm 3: Annealing-based Alternation Algorithm for Subset Selection on Manifolds
#-----------------------------------------------------------------------------------------
#Input: 
    #1. Data points X = {x1, x2, . . . , xn} ∈ M, 
    #2. Number of exemplars k, 
    #3. Tolerance step δ
#Output: 
    #1. E = {e1, . . . ek} ⊆ X

def proposed_algorithm( dataPoints , exemplars, tolerance ):
    
    #Initial setup:
    # - Compute intrinsic mean µ of X
    intrinsicMean = 0.0 
    for data in dataPoints:
        intrinsicMean += data
    intrinsicMean /= len(dataPoints)
    # - Compute tangent vectors vi ← logµ(xi)
    vector = []
    count = 0
    for data in dataPoints:
        vector[count] = math.log(data, intrinsicMean)
        count += 1

    # - V ← [v1, v2, . . . , vn]
    Vee = vector
    # - ω ← [1, 2, . . . , n] be the 1 × n index vector of X
    wee = []
    count = len(dataPoints)
    for x in range(count):
        wee[x] = x
    tol = 1
    #Initialize:
    # - Π ← Randomly permute columns of In×n
    pie1 = np.identity(len(dataPoints))
    pie2 = np.random.rand(len(dataPoints))
    #Update:
    Vee = np.multiply( Vee, pie )
    wee = np.multiply( wee, pie )

    #while Π != In×n do
    while compare2matrix(pie, identity):
        #Diversity: Π ← Div(V, k, tol) as in algorithm 2.
        pie = Div( Vee, exemplars, tol)

        #Update: V ← V Π, ω ← ωΠ.
        Vee = np.multiply( Vee, pie )
        wee = np.multiply( wee, pie )

        #Representative Error: Π ← Rep(X, k, ω,1) as in algorithm 1
        pie = Rep( dataPoints, exemplars, wee, 1)

        #Update: V ← V Π, ω ← ωΠ.
        Vee = np.multiply( Vee, pie )
        wee = np.multiply( wee, pie )
        tol = tol + tolerance
    
    # - ei ← xωi for i = {1,2,. . . ,k}
    Eee = []
    for x in range(exemplars):
        Eee[x] = wee[x]
    return Eee


#----------------------------------------------------------------------------------------
#   Comparing Two matrices - true if they equal false otherwise
#----------------------------------------------------------------------------------------
def compare2matrix(one,two):
    
    count = len(one)
    while count > 0
        if np.array_equal( one[count] , two[count] )
            return False
        count -= 1
    return True


#----------------------------------------------------------------------------------------
#   Algorithm 2: Algorithm for Diversity Maximization
#----------------------------------------------------------------------------------------
#Input: 
    #1. Matrix V ∈ Rd×n
    #2. k 
    #3. Tolerance tol
#Output: 
    #1. Permutation Matrix Π

def Diversity(matrix, k, tol):
Initialize Π ← In×n
repeat
Compute QR decomposition of V to obtain
R11, R12 and R22 s.t., V = Q
( R11 R12
  0   R22 )
βij ←q(R−1 11 R12) 2 ij + || R22αj ||2 2||αTi R−1 11 ||2 2 
βm ← maxij βij
(ˆi, ˆj) ← arg maxijβij
Update: Π ← Π Πi↔(j+k)
V ← V Πi↔(j


#----------------------------------------------------------------------------------------
#   Algorithm 1: Algorithm to minimize Jrep
#----------------------------------------------------------------------------------------

