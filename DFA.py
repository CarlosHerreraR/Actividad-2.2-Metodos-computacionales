#Actividad 2.2 Programando un DFA
#Autores: 
#Alberto Cebreros González A01798671
#Carlos Yahir Herrera Rodríguez A01798203

def dfa_test(input_filename, test_filename):
    # Leer la especificación del DFA del archivo de entrada
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        alphabet = eval(lines[0].strip())
        num_states = int(lines[1].strip())
        accepting_states = set(eval(lines[2].strip()))
        transitions = [list(map(int, eval(line.strip()))) for line in lines[3:]]

    # Leer las cadenas de prueba del archivo de test
    with open(test_filename, 'r') as file:
        test_strings = file.read().strip().split('\n')

    # Evaluar las cadenas de prueba
    results = []
    for string in test_strings:
        current_state = 0
        for character in string:
            if character in alphabet:
                current_state = transitions[current_state][alphabet.index(character)]
            else:
                current_state = None
                break
        results.append('A' if current_state in accepting_states else 'R')

    # Escribir los resultados en un archivo de salida
    output_filename = f'{test_filename.split(".")[0]}-output.txt'
    with open(output_filename, 'w') as file:
        for result in results:
            file.write(result + '\n')

    print(f'Results written to {output_filename}')

# Ejemplo de uso
dfa_test('dfa-01.txt', 'test-01.txt')
