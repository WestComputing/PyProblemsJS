function tickets(peopleInLine) {
    const ticketPrice = 25;
    const cashRegister = [];
    for (const cash of peopleInLine) {
        let index = 0;
        let change = cash - ticketPrice;
        while (change && index < cashRegister.length) {
            if (change >= cashRegister[index]) {
                change -= cashRegister[index];
                cashRegister.splice(index, 1);
            } else {
                index++;
            }
        }
        if (change) {
            return "NO";
        } else {
            cashRegister.push(cash);
            cashRegister.sort((a, b) => b - a);
        }
    }
    return "YES"
}

console.log(tickets([25, 25, 50, 50]), "YES");
console.log(tickets([25, 100]), "NO");