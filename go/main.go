package main

import  (
            "os"
            "fmt"
            "io/ioutil"
            "log"
            "bufio"
        )

func main(){
    cl_args := os.Args[1:]
    if len(cl_args) > 1{
        fmt.Println(`
Usage:
    dexter <program_file_path> - to run a dexter program written in file.
    dexter - to run dexter interactive prompt.
`)
    }else if len(cl_args) == 1{
        runFile(cl_args[0])
    }else{
        runPrompt()
    }
}

func runFile(source_file string){
    file, err := os.Open(source_file)
    if err != nil{
        log.Fatal(err)
    }
    defer file.Close()

    source_code, err := ioutil.ReadAll(file)
    run(string(source_code))
}

func runPrompt(){
    reader := bufio.NewReader(os.Stdin)
    for{
        fmt.Print("--> ")
        code, _ := reader.ReadString('\n')
        run(code)
    }
}

func run(text string){
    scanner := NewScanner(text)
    tokens := scanner.scanTokens(text)
    for(index:=0; index<len(tokens); index++){
        fmt.Println(tokens[index])
    }
}

func showError(line_number int, message string){
    report(line_number, "", message)
}

func report(line_number int, where string, message string){
    fmt.Prinf("line %d > Error: %s -> %s", line_number, where, message)
}
