package main

import (
    "os"
    "fmt"
    "aoc23/calendar"
    // "strconv"
)

func main() {
    run := os.Args[1]

    // num,_ := strconv.ParseUint(input, 10, 64)
    // num,_ := strconv.Atoi(input)
    
    // var nums []int
    // for _,v := range input {
    //     num,_ := strconv.Atoi(v)
    //     nums = append(nums, num)
    // }
    var result int

    if run == "1" {
        result = calendar.Day01(calendar.Day01Example)
    } else{
        result = calendar.Day01(calendar.Day01Example)
    }

    fmt.Println(result)

    // var r []rune
    // for _,s := range input {
    //     r = append(r,s)
    // }
    // fmt.Println(kata.IsValidWalk(r))

    // fmt.Println(kata.RemovNb(num))
}
