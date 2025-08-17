use proconio::input;

fn main() {
    input! {
        n: usize,
    };

    let mut left = 1_000_000_000;
    let mut right = 0;
    let mut top = 1_000_000_000;
    let mut bottom = 0;

    for _ in 0..n {
        input! {
            y: usize,
            x: usize,
        }
        left = left.min(x);
        right = right.max(x);
        top = top.min(y);
        bottom = bottom.max(y);
    }

    let a = (right - left + 1) / 2;
    let b = (bottom - top + 1) / 2;
    println!("{}", a.max(b));
}   