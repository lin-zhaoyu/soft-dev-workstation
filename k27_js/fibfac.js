// Team Blue Duck :: Zhao Yu Lin, Sean Ging
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-03
// --------------------------------------------------


var fact = function(n){
  if(n <= 1)
  return 1
  return (n * fact(n - 1))
};

var fib = (n) => {
  if(n <= 1)
  return n
  else{
    return (fib(n - 1) + fib(n + 2))
  }
}


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
