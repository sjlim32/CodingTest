// 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
// numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

const solution = (numbers) => {
	const answer = numbers.sort(function(a, b) {return b - a})
	return answer[0] * answer[1]
}

// sort는 O(nlogn), 배열의 최댓값만 찾는 것이 O(n)이므로 효율적

const solution2 = (numbers) => {
	const answer = numbers.sort((a,b) => b-a)
	return answer[0] * answer[1]
}

console.log(solution([1, 2, 3, 4, 5]))
console.log(solution([0, 31, 24, 10, 1, 9, 30]))