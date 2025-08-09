use proconio::input;
fn main() {
    input! {
        s: String
    };

    let s_chars: Vec<char> = s.chars().collect();

    let mut ans: f64 = 0.0;
    for i in 3..=s.len() {
        for window in s_chars.windows(i) {
            if let (Some(&'t'), Some(&'t')) = (window.first(), window.last()) {
                let count_t = window.iter().filter(|&&c| c == 't').count();
                let fill_rate = (count_t as f64 - 2.0) / (i as f64 - 2.0);
                ans = ans.max(fill_rate);
            }
        }
    }
    println!("{}", ans);
}
