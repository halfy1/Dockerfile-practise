fn main() {
    println!("Hello from Rust CLI!");
    let args: Vec<String> = std::env::args().collect();
    if args.len() > 1 {
        println!("Got arguments: {:?}", &args[1..]);
    }
    // Here you might simulate a loop or do some work until SIGINT is received
}