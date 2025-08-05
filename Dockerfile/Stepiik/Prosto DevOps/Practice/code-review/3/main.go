package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go Docker container!")
}

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    http.HandleFunc("/", handler)
    log.Printf("Starting server on port %s...", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}