import inspect
import itertools


def truth_table(*predicates):
    for predicate in predicates:
        signature = inspect.signature(predicate)
        combinations = list(itertools.product([True, False], repeat=len(signature.parameters)))
        params_names = list(signature.parameters)
        title = " | ".join(params_names + ["result"])
        print(title)
        print('-' * len(title))
        for combination in combinations:
            print("| ".join(
                [str(int(param_value)) + " " * len(param_name)
                 for
                 param_value, param_name in zip(combination, params_names)] + [str(int(predicate(*combination)))]))
        print()


def compare_predicates(*predicates):
    signature = inspect.signature(predicates[0])
    assert (len(predicates) > 1)

    # predicates should have the same signature
    for predicate in predicates:
        if len(signature.parameters) != len(inspect.signature(predicate).parameters):
            return False

    combinations = list(itertools.product([True, False], repeat=len(signature.parameters)))
    for i in range(1, len(predicates)):
        for combination in combinations:
            if predicates[0](*combination) != predicates[i](*combination):
                return False
    return True


def first(p, q, r):
    # ((p->q)->r) <-> (r->(q^p))
    l_statement = not (p and not q)  # p->q
    l_statement = not (l_statement and not r)  # (l_statement)->r

    r_statement = q and p  # q^p
    r_statement = not (r and not r_statement)  # (r->r_statement)

    return (l_statement and r_statement) or (not l_statement and not r_statement)


def a(p, q):
    # p->q
    return not (p and not q)


def b(p, q):
    # -(p^(-q))
    return not (p and (not q))


def c(p, q):
    # (-p)Uq
    return (not p) or q


def main():
    truth_table(first)


if __name__ == "__main__":
    print(compare_predicates(a, b, c))
