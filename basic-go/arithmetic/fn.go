package main

import "fmt"

func main() {
	angka := 1

	sum(angka)
	subs(angka)
	div(angka)
	mult(angka)
}

func sum(a int) {
	fmt.Println(a + a)
}

func subs(a int) {
	fmt.Println(a - a)
}

func div(a int) {
	fmt.Println(a / a)
}

func mult(a int) {
	fmt.Println(a * a)
}
