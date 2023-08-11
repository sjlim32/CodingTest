// 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

const solution = num_list => {
	let even = []
	let odd = []
	num_list.map(n => n % 2 === 0 ? even.push(n) : odd.push(n))

	return [even.length, odd.length]
}

// OTHER ANSWER

function solution2(num_list) {
	let answer = [0, 0];
	for(let a of num_list) {
		answer[a%2] += 1
	}
	return answer;
}

const solution3 = num_list => num_list.reduce((acc, cur) => ( cur & 1 ? acc[1]++ : acc[0]++, acc), [0, 0])

const solution4 = num_list => {
	return [
		num_list.filter(n => n % 2 === 0).length,
		num_list.filter(n => n % 2 === 1).length
	];
}