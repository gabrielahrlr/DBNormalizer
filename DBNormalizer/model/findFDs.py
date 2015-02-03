__author__ = 'Nantes'
from itertools import chain, combinations


def find_fds(attributes, db_partition, test_mode=False, pk=[], uk=[]):
    attr = attributes[:]
    len_attributes = attr.__len__()
    fds = {}
    for i in range(0, len_attributes):
        rhs = attr.pop(0)
        lhs_in = attr[:]
        # pk_unique = []
        # if set(pk).issubset(set(lhs_in)):
        #     pk_unique.append(pk)
        #     lhs_in = list(set(lhs_in) - set(pk))
        # for u in uk:
        #     if set(u).issubset(set(lhs_in)):
        #         pk_unique.append(u)
        #         lhs_in = list(set(lhs_in) - set(u))

        lhs = find_fds_rhs(lhs_in, [rhs], db_partition, test_mode)
        fds[rhs] = lhs # + pk_unique
        attr.append(rhs)
    return fds


def find_fds_rhs(lhs, rhs, db_partition, test_mode=False):
    """
    Finds all the minimal functional dependencies X->rhs with X subset of lhs. Usually lhs = U\rhs where U is the
    set of attributes in the relation. The idea of this function is to eliminate unnecessary computation using the
    fact that, if the fd X->E does not hold, then for all Y subset of X, Y->E doesn't hold either.

    db_partition doesn't play an important role in this function, it is passed to the function test_fd_db that
    determines if a given fd is satisfied by the data in db_partition.

    :param lhs: a list containing attributes in the lhs of a fd
    :param rhs: a list containing attributes in the rhs of a fd
    :param db_partition: a partition of a relation in SQL over which the dependencies are to be tested
    :return: a list with the minimal lhs that satisfy lhs->rhs
    """
    x = {tuple(lhs)}
    e0 = set()  # set with the non-satisfied fds
    e1 = set()  # set with the satisfied fds
    set_len = lhs.__len__()
    while x.__len__() != 0 and set_len > 0:
        level = set()  # each level tries the proper subsets of X with length len(X)-1
        for subx in x:
            if test_mode:
                test = test_fds_test(list(subx), rhs, db_partition)
            else:
                test = test_fds(list(subx), rhs, db_partition)
            if not test:
                e0 = e0.union([subx])
            else:
                e1 = set(remove_super_sets(list(subx), e1))  # removes redundancy in e1
                e1 = e1.union([subx])
                level = level.union([subx])

        level = set(subsets(list(level), set_len - 1))  # obtain the next level
        e0 = set(subsets(list(e0), set_len - 1))
        x = prune(level, e0)  # removes the cases that are not satisfiable by means of e0
        set_len -= 1
    return [list(x) for x in list(e1)]


def subsets(x, k):
    """
    Finds the subsets of cardinality k for each element (set) of the list x
    :param x: a list of sets
    :param k: integer
    :return: list of subsets
    """
    sub_set = set()
    for i in x:
        sub_set = sub_set.union(set(combinations(i, k)))
    return list(sub_set)


def prune(x, y):
    """
    Set difference
    :param x:
    :param y:
    :return:
    """
    return x - y


def test_fds_test(lhs, rhs, fds):
    """
    Tests if the fds lhs->rhs is satisfied in fds. This function is only for testing purposes
    :param lhs:
    :param rhs:
    :param fds:
    :return: boolean
    """
    closure = fds.attribute_closure(lhs)
    return rhs[0] in closure


def test_fds(lhs, rhs, relation_dict):

    lhs_partition = get_intersection(lhs, relation_dict)
    rhs_partition = get_intersection(rhs, relation_dict)
    x = True
    k = 0
    while x and k < len(lhs_partition):
        element = lhs_partition[k]
        y = False
        z = 0
        while not y and z < len(rhs_partition):
            y = set(element).issubset(set(rhs_partition[z]))
            z += 1
        x = y
        k += 1
    return x


# def get_intersection(attributes, relation_dict):
#     res = relation_dict[attributes[0]]
#     print("--entra intersection----")
#     for i in range(1, len(attributes)):
#         x = relation_dict[attributes[i]]
#         res = [set(a).intersection(set(b)) for a in res for b in x]
#         #res = list(filter(None, [list(set(a) & set(b)) for a in res for b in x]))
#     print("--sale intersection----")
#     return res

def get_intersection(attributes, relation_dict):
    res = relation_dict[attributes[0]]

    for i in range(1, len(attributes)):
        x = relation_dict[attributes[i]]
        res_list = []
        for i in x:
            len_i = len(i)
            k = 0
            while len_i > 0:
                j = res[k]
                inter = set(i).intersection(set(j))
                if len(inter) != 0:
                    len_inter = len(inter)
                    len_i = len_i - len_inter
                    res_list.append(list(inter))
                k += 1
        res = res_list

    return res


def remove_super_sets(sub_set, set_of_sets):
    """
    Removes the elements in set_of_sets that are super sets of sub_set
    :param sub_set: a set
    :param set_of_sets: list of sets
    :return: list of sets
    """
    return [x for x in set_of_sets if not set(x).issuperset(set(sub_set))]


# print(find_fds_rhs(['essn', 'sex', 'dependent_name', 'bdate'], ['relationship'], {'sex': [[1, 3, 6, 7], [2, 4, 5]],
#                                                                                    'bdate': [[2], [6], [7], [3], [1],
#                                                                                              [4], [5]],
#                                                                                    'essn': [[1, 2, 3], [5, 6, 7], [4]],
#                                                                                    'relationship': [[3, 4, 7], [1, 6],
#                                                                                                     [2, 5]],
#                                                                                    'dependent_name': [[1, 6], [5], [2],
#                                                                                                       [7], [4], [3]]},test_mode= False))

