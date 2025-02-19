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
//type User = {Weight:float; Height:float}

//let calculateBMI user =
//    let heightMeters = user.Height /100.0
//    user.Weight / (heightMeters ** 2.0)

//let categoryBMI bmi  =
//    if bmi <18.5 then "niedowaga"
//    elif bmi <24.9 then "waga prawidłowa"
//    elif bmi < 29.9 then "nadwaga"
//    else "morbidly obese Peter Griffin type "

//let rec readFloat prompt =
//    printfn "%s" prompt
//    match Double.TryParse(Console.ReadLine()) with
//    | (true, value) -> value
//    | _ -> 
//        printfn "Użyj poprawnych danych"
//        readFloat prompt

//let main() =
//    let weight = readFloat "Podaj wagę w kg"
//    let height = readFloat "Podaj wzrost w cm"
//    let user = {Weight = weight; Height = height}
//    let bmi = calculateBMI user
//    printfn "Twoje BMI wynosi: %.2f" bmi
//    printfn "Kategoria BMI to: %s" (categoryBMI bmi)
//main()

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


//-----------------------------------------------------------
// LAB2

////Zad1
//printfn "Podaj tekst"
//let inputText = Console.ReadLine();
//let countWords(text: string) =
//    text.Split([|' ' ; '\t' ; '\n' ; ';' ; ':' ; '.'|],StringSplitOptions.RemoveEmptyEntries)
//    |>Array.length

////spacje 

//let countCharts (text: string)=
//    text.Replace(" ", "").Length

//let wordsCount = countWords inputText
//let charsCount = countCharts inputText

//printfn "Liczba słów: %d" wordsCount
//printfn "Liczba znaków: %d" charsCount

////Zad2 

//printfn "Podaj tekst"
//let inputPalindrom = Console.ReadLine()


//let isPalindrom (text: string)=
//    let clearText = text.Replace(" ", "").ToLower()
//    clearText = String(Array.rev (clearText.ToCharArray()))

//if isPalindrom inputPalindrom then
//    printf"jest"
//else
//    printfn"niejest"

//zad3

//let inputText = Console.ReadLine()

//    let areDuplicatsintajszi(text: string) =
//        let clearText =  text.Replace(" ", "").ToLower()
//        clearText = String(Array).ToCharArray()

//[<EntryPoint>]

//let main argv =

    


//    0




type Osoba(imie: string, wiek: int) =
    member this.Imie = imie
    member this.Wiek = wiek
    member this.Info() = printfn"Witaj %s , pushujesz %d lat" this.Imie this.Wiek

let osoba1 = Osoba("Pioczruś",30)
osoba1.Info()

type Student(imie: string, wiek: int, numeralbumu: int)=
    inherit Osoba(imie,wiek)
    member this.numeralbumu = numeralbumu
    
let student = Student("Pioczruś",30,68299)

[<AbstractClass>]

type Figura()=
    abstract Pole: unit -> float
    abstract Obwod: unit -> float

type Kolo(promien :float) =
    inherit Figura()
    override this.Pole (): float = Math.PI * promien *promien
    override this.Obwod (): float = 2.0 * Math.PI * promien
        
let kolo = Kolo(27.5)

printfn "pole to %.2f, obwód to %.2f" (kolo.Pole()) (kolo.Obwod())

type IFigura = 
    abstract Opis: unit -> unit


type kwadrat() =
    interface IFigura with
     member this.Opis() = printfn "To jest kwadrat"

let kw = kwadrat() :> IFigura
kw.Opis()