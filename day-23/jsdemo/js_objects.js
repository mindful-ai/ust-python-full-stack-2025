Welcome to Node.js v12.14.0.      
Type ".help" for more information.
> var o = var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
Thrown:
var o = var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
        ^^^

SyntaxError: Unexpected token 'var'
> var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
undefined
>
> person
{ firstName: 'John', lastName: 'Doe', age: 50, eyeColor: 'blue' }
> typeof(person)
'object'
>
> var p = new Object()
undefined
> typeof(p)
'object'
> p.fname = "Jane"
'Jane'
> p.lname = "Doe"
'Doe'
> p.age = 35
35
> p.company = "Oracle"
'Oracle'
> p
{ fname: 'Jane', lname: 'Doe', age: 35, company: 'Oracle' }
>
>
> p.fname
'Jane'
> p['fname']
'Jane'
>
> p.fname = 'John'
'John'
> p
{ fname: 'John', lname: 'Doe', age: 35, company: 'Oracle' }
> p.country
undefined
> p.country = 'India'
'India'
> p
{
  fname: 'John',
  lname: 'Doe',
  age: 35,
  company: 'Oracle',
  country: 'India'
}
> p.fullname = function(){ return p.lname + ', ' + o.fname; }
[Function]
> p
{
  fname: 'John',
  lname: 'Doe',
  age: 35,
  company: 'Oracle',
  country: 'India',
  fullname: [Function]
}
> p.fullname()
Thrown:
ReferenceError: o is not defined
    at Object.p.fullname (repl:1:50)
> p.fullname
[Function]
> p.fullname = function(){ return p.lname + ', ' + p.fname; }
[Function]
> p.fullname()
'Doe, John'
>
> Object
[Function: Object]
> Object.keys(p)
[ 'fname', 'lname', 'age', 'company', 'country', 'fullname' ]
> Object.values(p)
[ 'John', 'Doe', 35, 'Oracle', 'India', [Function] ]
>
> // ----------------------------- constructor for an object
undefined
>
>
> function person(fname, lname, age, company){
... this.fname = fname;
... this.lname = lname;
... this.age = age;
... this.company = company;
... }
undefined
> person
[Function: person]
> var p1 = person("Anil", "Kumar", 35", "Oracle")
Thrown:
var p1 = person("Anil", "Kumar", 35", "Oracle")
                                 ^^

SyntaxError: missing ) after argument list
> var p1 = person("Anil", "Kumar", 35, "Oracle")
undefined
> var p2 = person("Sunil", "Kumar", 36, "Infosys")
undefined
> p1
undefined
> p2
undefined
> var p1 = new person("Anil", "Kumar", 35, "Oracle")
undefined
> p1
person { fname: 'Anil', lname: 'Kumar', age: 35, company: 'Oracle' }
> var p2 = new person("Sunil", "Kumar", 36, "Infosys")
undefined
> p2
person { fname: 'Sunil', lname: 'Kumar', age: 36, company: 'Infosys' }
>
> p1.addr = new Object()
{}
> p1
person {
  fname: 'Anil',
  lname: 'Kumar',
  age: 35,
  company: 'Oracle',
  addr: {}
}
> p1.addr.place = "Bangalore"
'Bangalore'
> p1.addr.phone = "+917342682374"
'+917342682374'
> p1
person {
  fname: 'Anil',
  lname: 'Kumar',
  age: 35,
  company: 'Oracle',
  addr: { place: 'Bangalore', phone: '+917342682374' }
}
> p2
person { fname: 'Sunil', lname: 'Kumar', age: 36, company: 'Infosys' }
> p1.addr.phone
'+917342682374'
>
>
> // e1, e2, e3 ...
undefined
> // c
undefined
>
> p1
person {
  fname: 'Anil',
  lname: 'Kumar',
  age: 35,
  company: 'Oracle',
  addr: { place: 'Bangalore', phone: '+917342682374' }
}

> delete p1.age
true
> p1
person {
  fname: 'Anil',
  lname: 'Kumar',
  company: 'Oracle',
  addr: { place: 'Bangalore', phone: '+917342682374' }
}
>