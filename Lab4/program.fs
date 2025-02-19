open System

type UserData = { Weight: float; Height: float }

let calculateBMI (user: UserData) =
    let heightInMeters = user.Height / 100.0
    user.Weight / (heightInMeters ** 2.0)

let categorizeBMI bmi =
    match bmi with
    | x when x < 18.5 -> "Niedowaga"
    | x when x < 24.9 -> "Prawidłowa waga"
    | x when x < 29.9 -> "Nadwaga"
    | _ -> "Otyłość"


printf "Podaj wagę (kg): "
let weight = Console.ReadLine() |> float
printf "Podaj wzrost (cm): "
let height = Console.ReadLine() |> float

let user = { Weight = weight; Height = height }
let bmi = calculateBMI user
let category = categorizeBMI bmi

printfn "Twoje BMI: %.2f (%s)" bmi category




let exchangeRates = 
    Map [
        ("USD", Map [("EUR", 0.85); ("GBP", 0.75)])
        ("EUR", Map [("USD", 1.18); ("GBP", 0.88)])
        ("GBP", Map [("USD", 1.33); ("EUR", 1.14)])
    ]

let convertCurrency amount fromCurrency toCurrency =
    match exchangeRates.TryFind fromCurrency with
    | Some rates when rates.ContainsKey toCurrency -> amount * rates.[toCurrency]
    | _ -> printfn "Nieznana para walutowa"; 0.0


printf "Podaj kwotę: "
let amount = Console.ReadLine() |> float
printf "Podaj walutę źródłową (USD, EUR, GBP): "
let fromCurrency = Console.ReadLine().ToUpper()
printf "Podaj walutę docelową (USD, EUR, GBP): "
let toCurrency = Console.ReadLine().ToUpper()

let result = convertCurrency amount fromCurrency toCurrency
if result <> 0.0 then
    printfn "Przeliczona kwota: %.2f %s" result toCurrency



let countWords (text:string) =
    text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries) |> Array.length

let countCharacters (text:string) =
    text.Replace(" ", "").Length

let mostFrequentWord (text:string) =
    text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.countBy id
    |> Array.sortByDescending snd
    |> Array.tryHead


printf "Wprowadź tekst: "
let input = Console.ReadLine()

printfn "Liczba słów: %d" (countWords input)
printfn "Liczba znaków (bez spacji): %d" (countCharacters input)

