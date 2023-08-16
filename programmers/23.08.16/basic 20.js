const solution = (s1, s2) => {
  const answer = s1.filter((n) => s2.includes(n));
  return answer.length;
};

// OTHER SOLUTION

const solution2 = (s1, s2) => {
  const concat = [...s1, ...s2];
  const setConcat = Array.from(new Set(concat));

  return concat.length - setConcat.length;
};
