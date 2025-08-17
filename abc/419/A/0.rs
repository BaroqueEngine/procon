use std::collections::HashMap;

use proconio::{input};
fn main() {
    input! {
        s: String,
    };

    let mut dic = HashMap::new();
    dic.insert("red".to_string(), "SSS");
    dic.insert("blue".to_string(), "FFF");
    dic.insert("green".to_string(), "MMM");

    let result = dic.get(&s);
    let ans = result.unwrap_or(&"Unknown");

    println!("{}", ans);
}
