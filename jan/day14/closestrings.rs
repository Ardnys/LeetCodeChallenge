impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        let mut word1_freq = vec![0; 26];
        let mut word2_freq = vec![0; 26];

        for c in word1.chars() {
            word1_freq[(c as u8 - b'a') as usize] += 1;
        }
        for c in word2.chars() {
            word2_freq[(c as u8 - b'a') as usize] += 1;
        }

        for i in 0..26 {
            if (word1_freq[i] != 0) != (word2_freq[i] != 0) {
                return false;
            }
            
        }
        word1_freq.sort_unstable();
        word2_freq.sort_unstable();

        word1_freq == word2_freq    }
}
