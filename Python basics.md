# Python Basics

## Size of an array
``` 
 len(a)
```
## For
``` 
for i in range(x):
        ____   
for animal in animals:
    if animal == 'Bird':
        print('Chirp!')
``` 
## While
``` 
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
``` 
## Diccionarios
``` 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

---- Get value with Key
x = thisdict.get("model")

---- GetKeys
x = thisdict.keys()

---- GetValues
x = thisdict.values()

---- GetItems
x = thisdict.items()

---- Check if Key Exists
if "model" in thisdict:

---- Add Items
thisdict["color"] = "red"

---- Update items
thisdict.update({"color": "red"})

---- Delete items
del thisdict["model"]
``` 

## Arrays
``` 
[]
---- Obtener el indice + elemento
for index,element in enumerate(array):

Add items
cars.append("Honda")

Remove items
cars.remove("Volvo")

count()
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position

** No devuelven nada sino que lo aplican al array
reverse()	Reverses the order of the list
sort()	Sorts the list
``` 

## Big O Cheat Sheet

# O(1)
When your algorithm is not dependent on the input size n
```
const firstElement = (array) => {
  return array[0];
};
```

# O(n)
ou get linear time complexity when the running time of an algorithm increases linearly with the size of the input. 
``` 
const calcFactorial = (n) => {
  let factorial = 1;
  for (let i = 2; i <= n; i++) {
    factorial = factorial * i;
  }
  return factorial;
};
```

# O(log n)
When the input size decreases on each iteration or step, an algorithm is said to have logarithmic time complexity.

```
const binarySearch = (array, target) => {
  let firstIndex = 0;
  let lastIndex = array.length - 1;
  while (firstIndex <= lastIndex) {
    let middleIndex = Math.floor((firstIndex + lastIndex) / 2);

    if (array[middleIndex] === target) {
      return middleIndex;
    }

    if (array[middleIndex] > target) {
      lastIndex = middleIndex - 1;
    } else {
      firstIndex = middleIndex + 1;
    }
  }
  return -1;
};
```

# O(n^2)
When you perform nested iteration, meaning having a loop in a loop, the time complexity is quadratic, which is horrible.
```
const matchElements = (array) => {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      if (i !== j && array[i] === array[j]) {
        return `Match found at ${i} and ${j}`;
      }
    }
  }
  return "No matches found 😞";
};
```

# O(2^n)
You get exponential time complexity when the growth rate doubles with each addition to the input (n), often iterating through all subsets of the input elements. Any time an input unit increases by 1, the number of operations executed is doubled.

```
const recursiveFibonacci = (n) => {
  if (n < 2) {
    return n;
  }
  return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
};

```