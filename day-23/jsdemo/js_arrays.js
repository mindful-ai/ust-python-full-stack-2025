Welcome to Node.js v12.14.0.
Type ".help" for more information.
>
>
>
> var L = ["mercedes", "bmw", "audi"]
undefined
> typeof(L)
'object'
>
> l[0]
Thrown:
ReferenceError: l is not defined
> L[0]
'mercedes'
> L[1]
'bmw'
> L[2] = "volvo"
'volvo'
> L
[ 'mercedes', 'bmw', 'volvo' ]
>
>
> // ---- Add elements in an array
undefined
>
> L
[ 'mercedes', 'bmw', 'volvo' ]
> L.push("audi")
4
> L
[ 'mercedes', 'bmw', 'volvo', 'audi' ]
> L.unshift("opel")
5
> L
[ 'opel', 'mercedes', 'bmw', 'volvo', 'audi' ]
>
> L.splice(3, 0, "hyundai")
[]
> L
[ 'opel', 'mercedes', 'bmw', 'hyundai', 'volvo', 'audi' ]
> L.splice(3, 0, "honda")
[]
> L
[
  'opel',    'mercedes',
  'bmw',     'honda',
  'hyundai', 'volvo',
  'audi'
]
> L.splice(3, 2, "honda")
[ 'honda', 'hyundai' ]
> L
[ 'opel', 'mercedes', 'bmw', 'honda', 'volvo', 'audi' ]
>
> // ------------------------ removing
undefined
>
> L.pop()
'audi'
> L
[ 'opel', 'mercedes', 'bmw', 'honda', 'volvo' ]
> L.shift()
'opel'
> L
[ 'mercedes', 'bmw', 'honda', 'volvo' ]
>
> L.splice(2, 2, ["audi", "opel"])
[ 'honda', 'volvo' ]
> L
[ 'mercedes', 'bmw', [ 'audi', 'opel' ] ]
> L.splice(2, 1, "audi", "opel")
[ [ 'audi', 'opel' ] ]
> L
[ 'mercedes', 'bmw', 'audi', 'opel' ]
> L
[ 'mercedes', 'bmw', 'audi', 'opel' ]
> L = [ 'mercedes', 'bmw', 'honda', 'volvo' ]
[ 'mercedes', 'bmw', 'honda', 'volvo' ]
> L.splice(2, 2, "audi", "opel")
[ 'honda', 'volvo' ]
> L
[ 'mercedes', 'bmw', 'audi', 'opel' ]
>
>
> // --------------------------------- rearrangement
undefined
>
> L
[ 'mercedes', 'bmw', 'audi', 'opel' ]
> L.sort()
[ 'audi', 'bmw', 'mercedes', 'opel' ]
> L.reverse()
[ 'opel', 'mercedes', 'bmw', 'audi' ]
> L
[ 'opel', 'mercedes', 'bmw', 'audi' ]
>
> // -------------------------------- slicing
undefined
> L.slice(1, 3)
[ 'mercedes', 'bmw' ]
> L
[ 'opel', 'mercedes', 'bmw', 'audi' ]
>