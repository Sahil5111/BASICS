use std::io;

fn main(){
    println!("enter a string.");
    let mut a=String::new();
    io::stdin()
        .read_line(&mut a)
        .expect("failed to read input.");
    println!("You entered {a}");
}