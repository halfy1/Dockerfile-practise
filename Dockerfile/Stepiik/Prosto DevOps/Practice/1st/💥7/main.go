package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go!")
}

func main() {
    http.HandleFunc("/", handler)
    port := "8080"
    log.Println("Starting server on port", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}