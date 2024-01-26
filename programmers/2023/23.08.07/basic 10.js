// 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
// 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

const solution = n => {
	let answer = n % 7
	console.log(answer)
	return answer > 0 ? ~~(n / 7) + 1 : n / 7
}

const solution2 = n => Math.ceil(n/7)

console.log(solution(7))
console.log(solution(1))
console.log(solution(15))