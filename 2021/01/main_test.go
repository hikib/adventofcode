package main

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	input, err := getInput("input_test.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

    result := part1(input)
	expected := "7"
    if result != expected {
        t.Error("result should be", expected, ", got", result)
    }
}

func TestPart2(t *testing.T) {
	input, err := getInput("input_test.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

    result := part2(input)
	expected := "5"
    if result != expected {
        t.Error("result should be", expected, ", got", result)
    }
}

