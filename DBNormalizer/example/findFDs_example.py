__author__ = 'Nantes'

from DBNormalizer.model.Relation import *

# Give fds of a hypothetical database (for testing purposes):
fd1 = FDependency(['A'], ['E']) # means A -> CD
fd2 = FDependency(['B'], ['C'])
fd5 = FDependency(['B'],['D'])
fd6 = FDependency(['A'],['D'])
fd7 = FDependency(['A'],['B'])
fd3 = FDependency(['C','D'], ['E'])
fd4 = FDependency(['C','D'],['B'])
fds = FDependencyList([fd1,fd2, fd3,fd4,fd5,fd6,fd7])
print(fds)
#print(fds)
#print(fds[0].lh)

# Finds the fds that satisfies the given lhs and rhs. The idea of this function is to eliminate unnecessary computation
# using th fact that, if the fd X->E does not hold, then for all Y subset of X, Y->E doesn't hold either.

# Creates a relation with only name and attributes
#relation1 = Relation('Test', ['A', 'B', 'C', 'D', 'E'])
# Find the fds in the database (for testing purposes suppose the database is one in which fds1 hold)
#print(relation1)
#relation1.find_fds(fds1, test_mode=True)
#print(relation1.fds)
#
def join_rhs(fds):
    new_fds = FDependencyList()
    old_fds = fds[:]
    while len(old_fds) > 0:
        fds_sel = old_fds.pop()
        i = 0
        while i < len(old_fds):
            fd = old_fds[i]
            if fds_sel.lh == fd.lh:
                fds_sel.rh = fds_sel.rh + fd.rh
                old_fds.pop(i)
            i+=1
        new_fds.append(fds_sel)
    return new_fds



#




    # for i in fds:
    #     print('i.lh',i.lh)
    #     if fds1[0].lh == i.lh:
    #         fds1.rh.append(i.rh)
    #
    #     else:
    #         print('sucks')
    #
    # return fds

print(join_rhs(fds))