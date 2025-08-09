use proconio::input;
fn main() {
    input! {
        n: usize,
        s: String
    };

    let result = if s.ends_with("tea") { "Yes" } else { "No" };
    println!("{}", result);
}
