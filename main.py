def run_game(sequence, limit=100):
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
            print("\nNever ending")
            print(len(res)-1, "steps in the cycle")
            for n in res:
                print(n)
            return step, res
        step += 1
    print("Ends")
    return step, [current]


if __name__ == '__main__':
    # Change this sequence to whatever you want
    sequence = [1,1,1,1,1,1,0,0,0,0,0,0]
    step_limit = 1000
    res = run_game(sequence, step_limit)
    print(res[0], "steps until this repeat")