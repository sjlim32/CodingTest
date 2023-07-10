function solution(citations) {
	citations.sort((a, b) => a - b);
	const length = citations.length
	let result = []

	for ( let i = 0; i <= length; i++ ) {
		const citation = citations.filter( v => v >= i).length
		if ( i <= citation) {
			result.push(i)
		}
	}

	return Math.max(...result)
}


console.log(solution([3, 0, 6, 1, 5])) // 3
console.log(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20])) // 길이 = 10 , 답 = 7
console.log(solution([6, 5, 5, 5, 3, 2, 1, 0])) // 길이 = 8, 답 = 4

0+1 <= 20
1+1 <= 19
2+1 <= 18
3+1 <= 17
4+1 <= 16
5+1 <= 15
6+1 <= 11
7+1 <= 5

