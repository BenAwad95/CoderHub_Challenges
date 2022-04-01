function maxElement(arr) {
    let max = arr[0]
    for (let index = 1; index < arr.length; index++) {
        if (arr[index] > max) {
            max = arr[index]
        }
        
    }
    return max
}

console.log(maxElement([4,7,5,7,4]))