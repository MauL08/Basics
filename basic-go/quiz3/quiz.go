package main

import "fmt"

func calculate(num1 int, num2 int, sign string) int {
	var cur int

	if sign == "+" {
		cur = num1 + num2
	}
	if sign == "-" {
		cur = num1 - num2
	}
	if sign == "*" {
		cur = num1 * num2
	}
	if sign == "/" {
		cur = num1 / num2
	}

	return cur
}

func main() {
	// scores := [...]int{10, 5, 8, 9, 7}

	// total := sum(scores)

	result := calculate(10, 2, "=")

	fmt.Println(result)
}
