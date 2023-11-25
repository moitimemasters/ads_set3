use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;

fn merge(arr: &mut Vec<i32>, left: usize, right: usize) {
    let mid = (left + right) / 2;
    let mut merged = Vec::new();
    let mut u0 = left;
    let mut u1 = mid + 1;
    while u0 <= mid && u1 <= right {
        merged.push(if arr[u0] <= arr[u1] {
            u0 += 1;
            arr[u0 - 1]
        } else {
            u1 += 1;
            arr[u1 - 1]
        });
    }

    while u0 <= mid {
        merged.push(arr[u0]);
        u0 += 1;
    }
    while u1 <= right {
        merged.push(arr[u1]);
        u1 += 1;
    }
    for i in left..=right {
        arr[i] = merged[i - left];
    }
}

fn standart_merge_sort(arr: &mut Vec<i32>, left: usize, right: usize) {
    if left >= right {
        return;
    }
    let mid = (left + right) / 2;
    standart_merge_sort(arr, left, mid);
    standart_merge_sort(arr, mid + 1, right);
    merge(arr, left, right);
}

fn insertion_sort(arr: &mut Vec<i32>, left: usize, right: usize) {
    for i in (left + 1)..=right {
        let key = arr[i];
        let mut j = (i - 1) as i32;
        while j >= 0 && key < arr[j as usize] {
            arr[j as usize + 1] = arr[j as usize];
            j -= 1;
        }
        arr[(j + 1) as usize] = key;
    }
}

fn hybrid_merge_sort(arr: &mut Vec<i32>, left: usize, right: usize, threshold: usize) {
    if right - left <= threshold + 1 {
        insertion_sort(arr, left, right);
        return;
    }
    let mid = (left + right) / 2;
    hybrid_merge_sort(arr, left, mid, threshold);
    hybrid_merge_sort(arr, mid + 1, right, threshold);
    merge(arr, left, right);
}

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let sort_type = &args[1];
    let file_path = &args[2];
    let threshold: usize = if sort_type == "hybrid" {
        args[3].parse().unwrap()
    } else {
        0
    };

    let mut contents = String::new();
    let mut file = File::open(file_path)?;
    file.read_to_string(&mut contents)?;
    let mut arr: Vec<i32> = contents
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let now = Instant::now();
    let arr_size = arr.len();
    if sort_type == "hybrid" {
        hybrid_merge_sort(&mut arr, 0, arr_size - 1, threshold);
    } else {
        standart_merge_sort(&mut arr, 0, arr_size - 1);
    }
    print!("{}", now.elapsed().as_micros());
    Ok(())
}
