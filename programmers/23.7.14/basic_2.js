// 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

function solution(n) {
	let answer= 0;

	for ( i=0; i<=n; i++) {
		if ( i % 2 === 0) {
			answer = answer + i
		}
	}

	return answer
}

// OTHER ANSWER

function solution2(n) {
	let half = Math.floor(n/2);
	return half*(half+1)
}

function solution3(n) {
	var answer = 0;
	for ( let i =2; i<=n; i+=2 ) {
		answer += i;
	}
	return answer;
}