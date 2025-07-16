def player(last_opponent_move, history=[], sequence_stats={}):
    if not last_opponent_move:
        last_opponent_move = 'R'

    history.append(last_opponent_move)
    next_guess = 'P'

    if len(history) > 4:
        recent_sequence = ''.join(history[-5:])
        sequence_stats[recent_sequence] = sequence_stats.get(recent_sequence, 0) + 1

        future_sequences = [
            ''.join(history[-4:] + [move])
            for move in ['R', 'P', 'S']
        ]

        guess_options = {
            seq: sequence_stats[seq]
            for seq in future_sequences if seq in sequence_stats
        }

        if guess_options:
            most_likely = max(guess_options, key=guess_options.get)
            next_guess = most_likely[-1]

    counter_move = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_move[next_guess]
