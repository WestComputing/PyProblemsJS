def scramble(s1, s2):
    char_tally = {}
    for char in s1:
        if char in char_tally:
            char_tally[char] += 1
        else:
            char_tally[char] = 1
    for char in set(s2):
        if char not in char_tally or char_tally[char] < s2.count(char):
            return False
    return True


print(scramble('rkqodlw', 'world'), True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
