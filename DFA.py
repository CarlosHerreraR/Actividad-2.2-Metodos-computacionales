def read_dfa(input_filename):
    with open(input_filename, 'r') as file:
        alphabet = file.readline().strip().strip('[]').replace("'", "").split(', ')
        num_states = int(file.readline().strip())
        acceptance_states = set(map(int, file.readline().strip().strip('[]').split(', ')))
        transitions = [list(map(int, line.strip().strip('[]').split(', '))) for line in file]
    return alphabet, num_states, acceptance_states, transitions

def evaluate_dfa(alphabet, acceptance_states, transitions, string):
    current_state = 0
    for character in string:
        if character not in alphabet:
            return False
        current_state = transitions[current_state][alphabet.index(character)]
    return current_state in acceptance_states

def dfa_test(input_filename, test_filename):
    alphabet, num_states, acceptance_states, transitions = read_dfa(input_filename)
    with open(test_filename, 'r') as file:
        test_strings = file.read().splitlines()
    
    output_filename = test_filename.replace('.txt', '-output.txt')
    with open(output_filename, 'w') as file:
        for string in test_strings:
            result = evaluate_dfa(alphabet, acceptance_states, transitions, string)
            file.write('A\n' if result else 'R\n')


dfa_test('dfa-03.txt', 'test-03.txt')


