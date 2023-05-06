fn reverse_words(str: &str) -> String {
    let reversed_words: Vec<String> = str
        .split(' ')
        .map(|word| word.chars().rev().collect())
        .collect();

    reversed_words.join(" ")
}
