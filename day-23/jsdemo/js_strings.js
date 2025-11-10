Welcome to Node.js v12.14.0.
Type ".help" for more information.
> var a = 10
undefined
> typeof(a)
'number'
> var s = "javascript"
undefined
> typeof(s)
'string'
> typeof(typeof(s))
'string'
> typeof(s) == 'string'
true
> typeof(s) == 'number'
false
> // ------------------------ Strings
undefined
> var s = "javascript"
undefined
> typeof(s)
'string'
> var s1 = new String("javascript")
undefined
> typeof(s)
'string'
> s == s1
true
> typeof(s1)
'object'
> s === s1
false
>
> s[0]
'j'
> s[1]
'a'
> s[0] = 'J'
'J'
> s
'javascript'
> s[2]
'v'
> s[2] = 'k'
'k'
> s
'javascript'
> s
'javascript'
> s.length
10
> s.indexOf("scr")
4
> s.lasIndexOf("scr")
Thrown:
TypeError: s.lasIndexOf is not a function
> s.lastIndexOf("scr")
4
> s1 = "javascrripscrt"
'javascrripscrt'
> s1.lastIndexOf("scr")
10
> s.search("scr")
4
> s.slice(4, 9)
'scrip'
> s.substr(4, 5)
'scrip'
> s.substring(4, 9)
'scrip'
>
> var text = "mary had a lit lab"
undefined
> text.replace("lit", "little")
'mary had a little lab'
> text.replace("lab", "lamb")
'mary had a lit lamb'
> s.toUpperCase()
'JAVASCRIPT'
> s.toLowerCase()
'javascript'
> s + " course"
'javascript course'
> s.concat(" ", "course", " ", "LVC")
'javascript course LVC'
> s2 = " hello  "
' hello  '
> s2.trim()
'hello'
>
> text = "mary had a little lamb"
'mary had a little lamb'
> text.split(' ')
[ 'mary', 'had', 'a', 'little', 'lamb' ]
> var words = text.split(' ')
undefined
> words
[ 'mary', 'had', 'a', 'little', 'lamb' ]
> typeof(words)
'object'
> words.join('-')
'mary-had-a-little-lamb'
>
> s.charAt(2)
'v'
> s.charCodeAt(2)
118
>