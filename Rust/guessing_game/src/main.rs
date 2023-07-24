use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
    loop {
        let mut str = String::new();
        println!("Input your guess");
        io::stdin()
            .read_line(&mut str)
            .expect("unable to read input");
        let guess: u32 = match str.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("invalid input");
                continue;
            }
        };
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("to small guess"),
            Ordering::Greater => println!("to big guess"),
            Ordering::Equal => {
                println!("You win");
                break;
            }
        }
    }
}
