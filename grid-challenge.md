Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Output Format

For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

Sample Input

    STDIN   Function
    -----   --------
    1       t = 1
    5       n = 5
    ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    fghij
    olmkn
    trpqs
    xywuv

Sample Output

    YES


#code:    

    def gridChallenge(grid):
      j=[]
      ans='YES'
      for i in grid:
        r=[c for c in (''.join(sorted(i)))]
        j.append(r)

    j = [[row[i] for row in j] for i in range(len(j[0]))]
    for i in j:
        if(sorted(i)!=i):
            ans='NO'
    return ans
