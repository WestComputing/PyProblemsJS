def generate_heaps_permutations(string: str) -> list:
    permutations = set()
    characters = [char for char in string]
    permutations.add(''.join(characters))
    call = [0] * len(characters)
    i = 0
    while i < len(characters):
        if call[i] < i:
            if i % 2:
                characters[call[i]], characters[i] = characters[i], characters[call[i]]
            else:
                characters[0], characters[i] = characters[i], characters[0]
            permutations.add(''.join(characters))
            call[i] += 1
            i = 0
        else:
            call[i] = 0
            i += 1
    return list(permutations)



print("['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']")
print(sorted(generate_heaps_permutations('aabb')))
