open System
open System.Collections.Generic

type linkedList<'T> =
    | Empty
    | Node of 'T * linkedList<'T>

let Head = 
    function
    | Empty -> failwith "Lista pusta"
    | Node(Head,_) -> Head

let Tail =
    function
    | Empty -> failwith "nie ma ogona"
    | Node(Tail,_)-> Tail

let addHead value list =
    Node(value, list)

let rec pristList list =
    match list with
    | Empty -> ()
    | Node (value, next) ->
        printf "%A" = value
        pristList next //rekurencja

[<EntryPoint>]

let main argv = 
    let list1 =  Empty
    let list2 = addHead 1 list1
    let list2 = addHead 2 list2


    pristList list2
    0