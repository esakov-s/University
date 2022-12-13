{
	#Тестовый калькультор
	add <- function(x, y){
		return(x + y)
	}
	subtract <- function(x, y){
		return(x - y)
	}
	multiply <- function(x, y){
		return(x * y)
	}
	divide <- function(x, y){
		if (y == 0){
			print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ', quote = FALSE)
			return('error')
		}
		return(x / y)
	}	
	pow <- function(x, y){
		return(x ^ y)
	}
	log1 <- function(x, y){
		if (y <= 0 | x == 1 | x <= 0){
			print('НЕПРАВИЛЬНАЯ ФОРМА ЗАПИСИ ЛОГАРИФМА', quote = FALSE)
			return('error')
		}
		return(log(x, base = y))
	}
	isch <- function(x, y){
		x <- as.integer(x)
		y <- as.integer(y)
		if (y <= 0 | x <= 0 | is.integer(x) == FALSE | is.integer(y) == FALSE){
			print('ПЕРЕВОД В ДРУГУЮ СИСТЕМУ СЧИСЛЕНИЯ НЕВОЗМОЖЕН', quote = FALSE)
			return('error')
		}
		t = 0
		p = 1
		while(x > 0){
			t <- p * x %% y + t
			p <- p * 10
			x <- x %/% y
		}
		return(t)
	}

	check <- function(a) {
		ch <- 0L
		for (i in a){
			if (i >= '0' & i <= '9' | i == '.' & ch < 1){
				if (i == '.' & ch < 1){
					ch <- 21L
				}
			}else {
				print(ch)
				return (FALSE)
			}
		}
		return(TRUE)
	}	
	
	######################################

	print("Выберите опрецаию:", quote = FALSE)
	print("1. Сложение", quote = FALSE)
	print("2. Вычитание", quote = FALSE)
	print("3. Умножение", quote = FALSE)
	print("4. Деление", quote = FALSE)
	print("5. Возведение в степень", quote = FALSE)
	print("6. Взятие логарифма(второго по снованию первого)", quote = FALSE)
	print("7. Перевод из десятичной системы счисления", quote = FALSE)
	print("! Выход из калькулятора")
	av <- c (1:7, '!')
	#print("Для использования предыдущего значения, при вводе числа напишите $x1 (если вместо первого), $x2 (если вместо второго), ", quote = FALSE)
	last <- 0.000001
	repeat{
		choice <- readline("Сделайте Ваш выбор, нажав [1/2/3/4/5/6/7] или завершите работу[!]:")
		if (choice == '!'){
			print('Работа программы калькулятор прекращена', quote = FALSE)
			break
		}
		if (choice %in% av == FALSE){
			print("Данной операции не существует. Выберите другую из приведённого списка", quote = FALSE)
			next
		}
		use = 3
		if (last != 0.000001){
			use <- as.integer(readline('Использовать предыдущие данные[1(вместо первого)/2(вместо второго)/3(не использовать)]?'))
		}
		choice <- as.integer(choice)
		a <- switch(use, last, readline("Введите первое число: "), readline("Введите первое число: "))
		b <- switch(use, readline("Введите второе число: "), last, readline("Введите второе число: "))
		
		if (check(a) == FALSE | check(b) == FALSE){
			print('Введён нечисловой аргумент. Повторите попытку ввода', quotes = FALSE)
			next
		}
		a <- as.numeric(a)
		b <- as.numeric(b)
		operation <- switch(choice, '+', '-', '*', '/', '^', 'log', 'в')
		result <- switch(choice, add(a, b), subtract(a, b), multiply(a, b), divide(a, b), pow(a, b), log1(a, b), isch(a, b))
		if (result == 'error'){
			next
		}
		print(paste(a, operation, b, '=', result), quote = FALSE)
		temp <- as.integer(readline("Сохранить результат в буфер? [1(да)/2(нет)]"))
		last <- switch(temp, result, last)
	}	
}


{
	print(log(8, 2))
}
