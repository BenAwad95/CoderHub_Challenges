function findElement(array, element) {
    let output = false;
    for (let index = 0; index < array.length; index++) {
        if (element == array[index]) {
            output = true;
            break;
        }
    }
    return output
}

console.log(findElement([1, 2, 3], 1))