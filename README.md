# conceptsofprog
Interpreter Programming Project
CS 3361 Concepts of Programming Languages
Below is the syntax and semantics for a single Boolean expression followed by
a period. Write a program which prompts the user to input a file name which
contains the Boolean expression or simply to input the string to be checked
(indicate which input method you will use in your comments). You may assume
that no input will be longer than 100 characters in length. Expressions may
contain white spaces and white spaces should be considered to be delimiters
(i.e. a white space between the − and > of the implication symbol would be a
syntax error). The program should check if the expression in the file is of valid
syntax and (if valid) compute the value of the expression. The output should
either be an error message or a a message that gives the value of the expression.
You must use the techniques taught in the class this is a recursive
descent interpreter.
Syntax: (note: for ∨ use the lowercase letter ”v” and for ∧ use the caret symbol)
Selection Sets
hBi ::= hITi . {∼, T, F,(}
hITi ::= hOTi hIT T aili {∼, T, F,(}
hIT T aili ::= − > hOTi hIT T aili {− >}
::= ε {.,)}
hOTi ::= hATi hOT T aili {∼, T, F,(}
hOT T aili ::= ∨ hATi hOT T aili {∨}
::= ε {− >, .,)}
hATi ::= hLi hAT T aili {∼, T, F,(}
hAT T aili ::= ∧ hLi hAT T aili {∧}
::= ε {∨, − >, .,)}
hLi ::= hAi {T, F,(}
::= ∼ hLi {∼}
hAi ::= T {T}
::= F {F}
::= ( hITi ) {(}
Syntactic Domains:
hBi : Bool stmt
hITi : Imply term
hOTi : Or term
hATi : And term
hIT T aili : Imply tail
hOT T aili : Or tail
hAT T aili : And tail
hLi : Literal
hAi : Atom
1
Semantic Domain:
b = {T.F} (Boolean values True and False)
Semantic Function Domains:
α : Bool stmt → b
β : Imply term → b
δ : Or term → b
γ : And term → b
λ : b × Imply tail → b
µ : b × Or tail → b
η : b × And tail → b
φ : Literal → b
ψ : Atom → b
Semantic Equations:
α( hITi. ) = β( hITi )
β( hOTihIT T aili ) = λ(δ( hOTi ),  hIT T aili )
δ( hATihOT T aili ) = µ(γ( hATi ),  hOT T aili )
γ( hLihAT T aili ) = η(φ( hLi ),  hAT T aili )
λ(b, ε) = b (where b ∈ {T, F})
λ(F,  − > hOTihIT T aili ) = λ(T,  hIT T aili )
λ(T,  − > hOTihIT T aili ) = λ(δ( hOTi ),  hIT T aili )
µ(b, ε) = b (where b ∈ {T, F})
µ(T,  ∨hATihOT T aili ) = T
µ(F,  ∨”hATihOT T aili ) = µ(γ( hATi ),  hOT T aili )
η(b, ε) = b (where b ∈ {T, F})
η(F,  ∧hLihAT T aili ) = F
η(T,  ∧hLihAT T aili ) = η(φ( hLi ),  hAT T aili )
φ(∼ hLi ) = if φ( hLi ) = T then F else if φ( hLi ) = F then T
φ( hAi ) = ψ( hAi )
ψ( T ) = T
ψ( F ) = F
ψ( (hITi) ) = (β( hITi ))
