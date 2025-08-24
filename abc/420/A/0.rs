use proconio::input;

fn main() {
    input! {
        mut x: usize,
        y: usize,
    };

    x += y;
    if x >= 13 {
        x -= 12
    }

    println!("{}", x);
}   