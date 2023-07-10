function solution(array, commands) {
    
    let answer = []
    
    for ( let command of commands ) {
        const [ a, b, c ] = command
        const newArr = array.slice(a-1, b).sort(function(a, b) { return a - b})
        console.log(newArr)
        answer.push(newArr[(c-1)])
    }
    
    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))