let rec fibonacci n =
    if n <= 1 then n
    else fibonacci (n - 1) + fibonacci (n - 2)

let fibonacciTail n =
    let rec helper a b count =
        if count = 0 then a
        else helper b (a + b) (count - 1)
    helper 0 1 n

printfn "Fibonacci(10) = %d" (fibonacci 10)
printfn "Fibonacci Tail(10) = %d" (fibonacciTail 10)



type Tree<'T> =
    | Empty
    | Node of 'T * Tree<'T> * Tree<'T>

let rec searchTree value tree =
    match tree with
    | Empty -> false
    | Node(v, left, right) ->
        if v = value then true
        elif value < v then searchTree value left
        else searchTree value right

let searchTreeIterative value tree =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node(v, left, right) :: rest ->
            if v = value then true
            else loop (left :: right :: rest)
    loop [tree]

let myTree = Node(10, Node(5, Empty, Empty), Node(15, Empty, Empty))
printfn "Wynik wyszukiwania 5: %b" (searchTree 5 myTree)
printfn "Wynik wyszukiwania iteracyjnego 15: %b" (searchTreeIterative 15 myTree)




let rec permutations list =
    match list with
    | [] -> [[]]
    | _ -> 
        list |> List.collect (fun x -> 
            permutations (List.filter ((<>) x) list) 
            |> List.map (fun perm -> x :: perm))

printfn "Permutacje listy [1;2;3]:"
permutations [1;2;3] |> List.iter (printfn "%A")


let rec hanoi n source auxiliary target =
    if n > 0 then
        hanoi (n - 1) source target auxiliary
        printfn "Przenieś krążek %d z %s do %s" n source target
        hanoi (n - 1) auxiliary source target

printfn "Wieże Hanoi dla 3 krążków:"
hanoi 3 "A" "B" "C"

