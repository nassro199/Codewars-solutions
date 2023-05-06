fn divisors(integer: u32) -> Result<Vec<u32>, String> {
    let mut divisors = Vec::new();
    for i in 2..integer {
        if integer % i == 0 {
            divisors.push(i);
        }
    }

    if divisors.is_empty() {
        Err(format!("{} is prime", integer))
    } else {
        Ok(divisors)
    }
}

