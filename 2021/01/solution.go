package main

import (
	"strconv"
)

func part1(input []string) string {
	count := 0
	prev := 0

	for i, num := range input {
		current, _ := strconv.Atoi(num)
		if i == 0 {
			prev = current
			continue
		}
		if current > prev { count++ }
		prev = current
	}
	return strconv.Itoa(count)
}

func part2(input []string) string {
	count := 0
	prev := 0
	nums := sliceAtoi(input)

	for i := 0; i <= len(input)-3; i++ {
		nums := nums[i:i+3]
		current := getSum(nums)
		if i == 0 {
			prev = current
			continue
		}
		if current > prev { count++ }
		prev = current
	}
	return strconv.Itoa(count)
}

func sliceAtoi(a []string) []int {
	out := make([]int, len(a))
	for i, str := range a {
		num, _ := strconv.Atoi(str)
		out[i] = num
	}
	return out
}

func getSum(a []int) int {
	sum := 0
	for _, num := range a { sum += num }
	return sum
}

