const cartas = ["sky striker","mistugiri", "vanquish k9"];

for (let i = 0; i < cartas.length; i++) {
    console.log(cartas[i]);
}

let wins = 10;

if (wins > 5) {
  console.log("Buen winrate");
}

let dano = 100;
let vida = 1000;

if (dano > vida) {
  console.log("El daño es mayor que la vida");
}
else {
  console.log("La vida es mayor que el daño");
}
function suma(a, b) {
  return a + b;
} 
console.log(suma(5, 10));
