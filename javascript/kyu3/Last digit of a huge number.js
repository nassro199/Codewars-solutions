function trueMod(a, n, m) {
    return Math.round( (a % m) * Math.pow( (a % m), (n + 3) % 4 ) ) % m;
}

function lastDigit(as){
    if (as.length == 0) return 1;
    let rightIsZero = false;
    let rightBiggerThan2 = false;
    let rightMod4 = 1;
    for (let i = as.length - 1; i > 0; --i) {
        console.log('With ' + i, as[i], rightIsZero, rightMod4);
        if (rightIsZero) {
            rightMod4 = 1;
            rightIsZero = false;
            rightBiggerThan2 = false;
        } else {
            rightMod4 =(rightBiggerThan2 && (as[i] % 4 === 2)) ? 0 : trueMod(as[i], rightMod4, 4);
             rightIsZero = as[i] === 0;
            rightBiggerThan2 = !rightIsZero && !(as[i] === 1)
        }
    }

    console.log(rightIsZero, rightMod4)

    return rightIsZero ? 1 : trueMod(as[0], rightMod4, 10);
}