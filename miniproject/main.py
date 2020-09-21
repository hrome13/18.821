def run_game(sequence, limit=100, verbose=True):
    def run_step(seq):
        new = []
        for n in range(len(seq) - 1):
            new.append(abs(seq[n] - seq[n + 1]))
        new.append(abs(seq[0] - seq[-1]))
        return new

    current = sequence
    step = 1
    monster = [current]
    first_indices = {tuple(current): 0}
    while step < limit and sum(current) != 0:
        current = run_step(current)
        monster.append(current)
        if tuple(current) not in first_indices:
            first_indices[tuple(current)] = step
        else:
            res = monster[first_indices[tuple(current)]:]
            if verbose:
                print("\nNever ending.", step-len(res), "until reaching cycle.")
                print(len(res)-1, "steps in the cycle.")
                for n in res:
                    print(n)
            return step, res, False
        step += 1
    if verbose:
        print("Ends in", step-1, "steps")
        print(monster)
    return step-1, [current], True

def length_four_grid_search(upper_int_limit, step_limit=100000):
    never_ending_sum = 0
    ending_sum = 0
    used = set()
    for a in range(upper_int_limit):
        if a%10 == 0:
            print("Current first term:", a)
        for b in range(upper_int_limit):
            for c in range(upper_int_limit):
                for d in range(upper_int_limit):
                    sequence = [a, b, c, d]
                    if tuple(sequence) not in used:
                        for n in range(4):
                            perm = sequence[n:]
                            perm.extend(sequence[:n])
                            used.add(tuple(perm))
                        if not run_game(sequence, step_limit, verbose=False)[2]:
                            never_ending_sum += 1
                        else:
                            ending_sum += 1
    print(never_ending_sum, "sequences found that never end.")
    print(ending_sum, "sequences found that end (not counting their permutations).")
    return never_ending_sum, ending_sum


if __name__ == '__main__':
    # Change this sequence to whatever you want
    sequence = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    step_limit = 100000
    res = run_game(sequence, step_limit)
    # length_four_grid_search(90)
