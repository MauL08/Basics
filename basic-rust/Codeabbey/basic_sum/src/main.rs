use proconio::input;

struct Bank {
   num1: i32,
   num2: i32,
}

fn main() {
    input! {
        a: i32,
        b: i32,
    }
    let sum = Bank {
        num1: a,
        num2: b,
    };
    println!("{}", sum.num1 + sum.num2);
}