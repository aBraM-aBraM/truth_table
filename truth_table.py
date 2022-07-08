import inspect
import itertools


def truth_table(predicate):
    signature = inspect.signature(predicate)
    combinations = list(itertools.product([True, False], repeat=len(signature.parameters)))
    print(" | ".join(list(signature.parameters) + ["result"]))
    print("------------------------")
    for combination in combinations:
        print(" | ".join([str(int(arg)) for arg in combination] + [str(int(predicate(*combination)))]))


def first(p, q, r):
    # ((p->q)->r) <-> (r->(q^p))
    l_statement = not (p and not q)  # p->q
    l_statement = not (l_statement and not r)  # (l_statement)->r

    r_statement = q and p  # q^p
    r_statement = not (r and not r_statement)  # (r->r_statement)

    return (l_statement and r_statement) or (not l_statement and not r_statement)


def main():
    truth_table(first)


if __name__ == "__main__":
    truth_table(first)
