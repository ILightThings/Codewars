fn main() {
let test: String = hor_mirror(String::from("Test\nanother\none"));
let newtest: String = vert_mirror(String::from("Test\nNew\nGame"));

println!("{}\n\n\n{}",test,newtest)
}

fn vert_mirror(s: String) -> String {
    let y = s.split("\n");
    let mut x: Vec<&str> = y.collect();
    let mut result = String::new();
    x.reverse();
    for word in x.iter(){
        result.push_str(word);
        result.push_str("\n")
    };
   String::from(result.trim())
}

fn hor_mirror(s: String) -> String {
    let y = s.split("\n");
    let x: Vec<&str> = y.collect();
    let mut result = String::new();
    for words in x.iter(){
        let orig_string: String = words.chars().rev().collect();
        result.push_str(&(orig_string+"\n"))
        };
        String::from(result.trim())
    }
    
 



