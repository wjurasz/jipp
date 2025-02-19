namespace MyNamespace

type MyClass(name: string) =
    member this.Name = name
    member this.Greet() = printfn "Hello, %s!" this.Name
