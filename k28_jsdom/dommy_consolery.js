/*
   your PPTASK:

   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.

    		Write with your future self or teammates in mind.

    		If you find yourself falling out of flow mode, consult
    		other teams
    		MDN

   A few comments have been pre-filled for you...

   (delete this block comment once you are done)
*/

// Team Green Granite::Zhao Yu Lin, Timber
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------

//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
var f = function (x) {
  var j = 30;
  return j + x;
};

//instantiate an object
var o = {
  name: "Thluffy",
  age: 15,
  items: [10, 20, 30, 40],
  morestuff: { a: 1, b: "ayo" },
  func: function (x) {
    return x + 30;
  },
};

var addItem = function (text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

var removeItem = function (n) {
  var listitems = document.getElementsByTagName("li");
  listitems[n].remove();
};

var red = function () {
  var items = document.getElementsByTagName("li");
  for (var i = 0; i < items.length; i++) {
    items[i].classList.add("red");
  }
};

var stripe = function () {
  var items = document.getElementsByTagName("li");
  for (var i = 0; i < items.length; i++) {
    if (i % 2 == 0) {
      items[i].classList.add("red");
    } else {
      items[i].classList.add("blue");
    }
  }
};

//insert your implementations here for...
//fact
var fact = (n) => {
  if (n <= 1) return 1;
  return n * fact(n - 1);
};

function displayFact(n) {
  let item = document.getElementById("fact");
  var x = fact(n);
  console.log(x + "HI");
  item.innerHTML = `fact(${n}) = ${x}`;
}
displayFact(5);

document.getElementById("facButton").addEventListener("click", count);

let count = 0;
function incrementFact() {
  count++;
  fact(count);
}
//fib
var fib = (n) => {
  if (n <= 1) return n;
  else {
    return fib(n - 1) + fib(n - 2);
  }
};
function displayFib(n) {
  let item = document.getElementById("fib");
  item.innerHTML = `fib(${n}) = ${fib(n)}`;
}
displayFib(12);
// GCD

var gcd = function (a, b) {
  let c = Math.max(a, b);
  let d = Math.min(a, b);

  if (c == 0) return d;
  if (d == 0) return c;
  return gcd(d, c % d);
}; //eucledian GCD
function displaygcd(a, b) {
  let item = document.getElementById("fib");
  item.innerHTML = `gcd(${a}, ${b}) = ${displaygcd(a, b)}`;
}
