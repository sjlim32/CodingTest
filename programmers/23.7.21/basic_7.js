// 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

const solution = num_list => num_list.reverse();

// OTHER ANSWER
function solution2 (num_list) {
	var answer = [];
	var j = num_list.length;

	for(let i = 1; i <= j; i++) {
		answer.push(num_list[j-i])
		// answer.push(num_list.pop())
	}

	return answer;
}


function solution3 (num_list) {
	return num_list.sort((a, b) => -1);
}