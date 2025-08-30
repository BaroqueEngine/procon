use proconio::input;

fn main() {
    input! {
      n: usize,
      s: [String; n],
      x: usize,
      y: String,
    }

    let result = if s[x - 1] == y {
      "Yes"
    }
    else {
      "No"
    };

    println!("{}", result);
}