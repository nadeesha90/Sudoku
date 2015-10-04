#sudoku solver
def check_constraints(mat):
#check rows
    for r in range(9):
        row = mat[r][0:9];
        bk = [];
        for e in row:
            if (e != 0):
                if (e in bk):
                    return False;
                else:
                    bk.append(e);

#check columns
    for c in range(9):
        col = mat[0:9][c];
        bk = [];
        for e in col:
            if (e != 0):
                if (e in bk):
                    return False;
                else:
                    bk.append(e);

#check squares
    indexes  = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)];
    for ix in indexes:
        sr = ix[0];
        sc = ix[1];
        bk = [];
        for r in range(3):
            for c in range(3):
                el = mat[sr+r][sc+c];
                if (el != 0):
                    if (el in bk):
                        return False;
                    else:
                        bk.append(el);

    #will return true for the empty assignment
    return True;

def iscomplete(mat):
    for r in range(9):
        for c in range(9):
            if(mat[r][c] == 0):
                return False;
    return True;

def check_row(mat,pos,val):
    r = pos[0];
    for x in range(9):
        if (mat[r][x] == val):
            return False;
    return True;

def check_col(mat,pos,val):
    c = pos[1];
    for x in range(9):
        if (mat[x][c] == val):
            return False;
    return True;

def check_square(mat,pos,val):
    sr = pos[0]/3;
    sc = pos[1]/3;
    for r in range(3):
        for c in range(3):
##            print (3*sr+r,3*sc+c);
            if (mat[3*sr+r][3*sc+c] == val):
                return False;
    return True;

def check_pos(mat,pos,val):
    row = check_row(mat,pos,val);
    col = check_col(mat,pos,val);
    sq = check_square(mat,pos,val);
    
    res = row and col and sq;
    
##    print "pos: " + str(pos[0]) + "," + str(pos[1]) + " val: " + str(val) + " result: " + str(res);
##    print "row: " + str(row) + " col: " + str(col) + " square: " + str(sq);
    return res;

def sel_unassigned_var(mat):
    for r in range(9):
        for c in range(9):
            if (mat[r][c] == 0):
                return (r,c);
            
def printmat(mat,depth):

    f.write("depth: " + str(depth) + "\n");
    for r in range(9):
        for c in range(9):
            f.write(str(mat[r][c]) + " ");
        f.write("\n");
    f.write("\n");

def matrix_copy(A):
    B = [];
    for i in range(len(A)):
        B.append([]);
    for i in range(len(A)):
        B[i] = A[i][:];
    return B;

def recursive_backtrack(mat,depth):
    if iscomplete(mat):
        return (mat,True);
   #print depth;
    pos = sel_unassigned_var(mat);
    for val in range(1,10):
        if (check_pos(mat,pos,val)):
            newmat = matrix_copy(mat);
            newmat[pos[0]][pos[1]] = val;
            result = recursive_backtrack(newmat,depth+1);
        #    printmat(newmat,depth);
            if (result != "failure"):
                return result;
    return "failure"
       

def stack_solve(mat):
    stack = [];
    stack.append(mat);
    while (len(stack) > 0):
        m = stack.pop();
        print m;
        if iscomplete(m):
            return (m,True);

        pos = sel_unassigned_var(m);
        printmat(m);
        for val in range(1,10):
            if (check_pos(m,pos,val)):
                newm = m[:];
                newm[pos[0]][pos[1]] = val;
                stack.append(newm);
    return "failure";
    
f = open("tempf.txt","w");

smat = [[0,0,0,0,0,4,7,9,8],[0,4,0,0,0,0,1,0,2],[0,0,0,2,0,1,0,0,5],[0,0,0,0,0,8,0,0,3],[0,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,7],[0,0,0,1,0,9,3,0,4],[0,0,4,0,0,0,0,2,0]];
    
#smat = [[0 for y in range(9)] for x in range(9)];
#smat[0][0] = 1;    
    
final_res = recursive_backtrack(smat,0);
print final_res;
printmat(final_res[0],0);
f.close();

