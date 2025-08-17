use std::collections::BinaryHeap;
use proconio::input;

fn main() {
    input! {
        q: i32,
    };

    let mut heap = BinaryHeap::new();
    for _ in 0..q {
        input! {
            query_type: i32,
        };

        if query_type == 1 {
            input! {
                x: i32,
            };
            heap.push(-x);
        }
        else {
            println!("{}", -heap.pop().unwrap());
        }
    }
}   