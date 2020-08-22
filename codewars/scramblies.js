function scramble(str1, str2) {
    const uniqueChars = new Set(str2);
    for (const char of uniqueChars) {
        const regex = new RegExp(`(${char})`, 'gi');
        if (str1.match(regex).length < str2.match(regex).length) {
            return false;
        }
    }

    return true;
}