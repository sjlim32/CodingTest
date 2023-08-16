// 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

function solution(my_string, letter) {
  return my_string
    .split("")
    .filter((n) => n !== letter)
    .join("");
}

// OTHER SOLUTION

const solution2 = (my_string, letter) => {
  return my_string.split(letter).join("");
};

const solution3 = (my_string, letter) => {
  return my_string.replaceAll(letter, "");
};
