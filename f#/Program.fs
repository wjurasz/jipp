open System
//Zadanie 1
//Console.WriteLine("Podaj masę ciała: ")
//let  masa_ciala = Console.ReadLine()|> Double.Parse

//Console.WriteLine("Podaj wzrost: ")
//let  wzrost = Console.ReadLine()
//let wzrost_float = Double.Parse(wzrost) / 100.0

//let liczenieBMI() =
//    masa_ciala / wzrost_float**2.0

//let BMI = liczenieBMI()

//printfn "Twoje BMI wynosi: %.2f" BMI

//wersja druga
type User = {Weight:float; Height:float}

let calculateBMI user =
    let heightMeters = user.Height /100.0
    user.Weight / (heightMeters ** 2.0)

let categoryBMI bmi  =
    if bmi <18.5 then "niedowaga"
    elif bmi <24.9 then "waga prawidłowa"
    elif bmi < 29.9 then "nadwaga"
    else "morbidly obese Peter Griffin type "

let rec readFloat prompt =
    printfn "%s" prompt
    match Double.TryParse(Console.ReadLine()) with
    | (true, value) -> value
    | _ -> 
        printfn "Użyj poprawnych danych"
        readFloat prompt

let main() =
    let weight = readFloat "Podaj wagę w kg"
    let height = readFloat "Podaj wzrost w cm"
    let user = {Weight = weight; Height = height}
    let bmi = calculateBMI user
    printfn "Twoje BMI wynosi: %.2f" bmi
    printfn "Kategoria BMI to: %s" (categoryBMI bmi)
main()

//Zadnie 2
//let kursy =
//    [ (("PLN", "USD"), 0.24)
//      (("USD", "PLN"), 4.13)
//      (("PLN", "EUR"), 0.23)
//      (("EUR", "PLN"), 4.26)
//      (("USD", "EUR"), 0.92)
//      (("EUR", "USD"), 1.09)
//      (("USD", "GBP"), 0.76)
//      (("GBP", "USD"), 1.32)
//      (("EUR", "GBP"), 0.83)
//      (("GBP", "EUR"), 1.20) ]
//    |> Map.ofList

//let wymiana kwota waluta_zr waluta_doc =
//    match kursy.TryFind (waluta_zr, waluta_doc) with
//    | Some kurs -> kwota * kurs
//    | None -> failwith "Nieobsługiwana waluta"

//Console.WriteLine("Podaj kwotę: ")
//let kwota = Console.ReadLine() |> Double.Parse

//Console.WriteLine("Podaj źródłową walutę (PLN, USD, EUR, GBP): ")
//let waluta_zr = Console.ReadLine().ToUpper()

//Console.WriteLine("Podaj docelową walutę (PLN, USD, EUR, GBP): ")
//let waluta_doc = Console.ReadLine().ToUpper()

//try
//    let kwota_po_wymianie = wymiana kwota waluta_zr waluta_doc
//    Console.WriteLine($"Przeliczona kwota to: {kwota_po_wymianie:F2} {waluta_doc}")
//with
//| ex -> Console.WriteLine($"Wystąpił błąd: {ex.Message}")

//Zadanie 3

//Console.WriteLine("Wprowadz tekst")
//let tekst = Console.ReadLine()

