use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut a: [usize; n],
        mut b: [usize; m],
    }

    b.sort();

    for target in &b {
        if let Some(index) = a.iter().position(|x| x == target) {
            a.remove(index);
        }
    }


    let joined_string = a.iter().map(|x| x.to_string())
    .collect::<Vec<String>>()
    .join(" ");

    println!("{}", joined_string);
}
