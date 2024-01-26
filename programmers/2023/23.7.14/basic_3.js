// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

const solution = n => n.reduce((a, c) => a + c, 0) / n.length;


// OTHER ANSWER
const solution2 = (numbers) => (numbers[0] + numbers[numbers.length - 1]) / 2
