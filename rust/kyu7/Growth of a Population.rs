fn nb_year(p0: i32, percent: f64, aug: i32, p: i32) -> i32 {
    let mut years = 0;
    let mut population = p0;

    while population < p {
        let increase = (population as f64 * percent / 100.0) as i32;
        population += increase + aug;
        years += 1;
    }

    years
}

fn main() {
    println!("{}", nb_year(1000, 2.0, 50, 1200)); // Output: 3
    println!("{}", nb_year(1500, 5.0, 100, 5000)); // Output: 15
    println!("{}", nb_year(1500000, 2.5, 10000, 2000000)); // Output: 10
}