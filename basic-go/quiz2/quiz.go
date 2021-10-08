package main

import "fmt"

func main() {
	// Mean
	task1()
	task2()
}

func task1() {
	score := [8]int{
		100,
		80,
		75,
		92,
		70,
		93,
		88,
		67}

	length := len(score)

	totalScore := 0

	for i := 0; i < 8; i++ {
		totalScore += score[i]
	}

	mean := totalScore / length

	fmt.Println(mean)
}

func task2() {
	var highScore [8]int

	score := [8]int{
		100,
		80,
		75,
		92,
		70,
		93,
		88,
		67}

	for i := 0; i < 8; i++ {
		if score[i] >= 90 {
			highScore[i] = score[i]
		}
	}

	for _, val := range highScore {
		if val != 0 {
			fmt.Print(val)
			fmt.Print(" ")
		}
	}
}
