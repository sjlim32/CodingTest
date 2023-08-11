// 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

const solution = my_string => my_string.split("").reverse().join("")


// OTHER ANSWER

const solution2 = my_string => {
	let answer = [...my_string].reverse().join("");
	return answer
}