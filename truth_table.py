import inspect
import itertools


def truth_table(predicate):
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

        
        
def first(first_param, second_param, third_param):
    # ((p->q)->r) <-> (r->(q^p))
    l_statement = not (first_param and not second_param)  # p->q
    l_statement = not (l_statement and not third_param)  # (l_statement)->r

    r_statement = second_param and first_param  # q^p
    r_statement = not (third_param and not r_statement)  # (r->r_statement)

    return (l_statement and r_statement) or (not l_statement and not r_statement)


def main():
    truth_table(first)


if __name__ == "__main__":
    truth_table(first)
