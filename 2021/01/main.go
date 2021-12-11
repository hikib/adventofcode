package main


import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	input, err := getInput("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Part1: ", part1(input))
	fmt.Println("Part2: ", part2(input))
}

func getInput(filename string) ([]string, error) {
	input, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	content := strings.Split(string(input[:]), "\n")
	return content, nil
}

