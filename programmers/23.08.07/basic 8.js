// x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
// x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
// x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
// x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
// x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 
// 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

function solution(dot) {
    let answer = 0
    // 둘의 형태가 같을 때
    dot[0] * dot[1] > 0 
        // x가 음수면 3, 양수면 1
        ? dot[0] + dot[1] < 0 
            ? answer = 3
            : answer = 1
    // 둘의 형태가 다를 때
        // x가 양수면 4, 음수면 2
        : dot[0] > dot[1]
            ? answer = 4 
            : answer = 2
    
    return answer
}

function solution2(dot) {
    return dot[0] > 0 ? dot[1] > 0 ? 1 : 4 : dot[1] > 0 ? 2 : 3
}

function solution3(dot) {
    const [num1, num2] = dot;
    const check = num1 * num2 > 0;
    return num1 > 0 ? ( check ? 1 : 4) : ( check ? 3 : 2)
}


console.log(solution3([2, 4]))
console.log(solution3([-2, 4]))
console.log(solution3([-2, -4]))
console.log(solution3([2, -4]))
