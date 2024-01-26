// 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

const solution = (n) => {
  let answer = n
    .toString()
    .split("")
    .reduce((acc, cur) => acc * 1 + cur * 1, 0);
  return parseInt(answer);
};

const solution2 = (n) => {
  return n
    .toString()
    .split("")
    .reduce((acc, cur) => acc + Number(cur), 0);
};
