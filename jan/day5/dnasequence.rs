impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let mut sequences = HashMap::new();
        let n = s.len();

        for i in 10..=n {
            if let Some(substr) = s.get(i-10..i) {
                *sequences.entry(substr).or_insert(0) += 1;
            }
        }

        sequences
            .iter()
            .filter(|&(_, val)| *val > 1)
            .map(|(key, _)| key.to_string())
            .collect()
    }
}
