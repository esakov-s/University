

{
	#Задание 1
	months <- c('января', 'февраля', 'марта', 'апреля', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')
	week <- c('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
	N <- as.integer(readline('Введите число N: '))

	#Ответ с использованием свойств векторов (проверить 1, 30, 100, 1000)
	year <- N %/% 360
	N <- N %% 365
	month <- N %/% 30 + 1
	day <- N %% 30
	print(paste0('Введённое число N', ' соответствует: ', day, ' ', months[month], ', ', week[(N - 1) %% 7 + 1], ', ', 21 + year, 'й год'))
	
	#Ответ с использованием циклов
	year <- 21
	month <- 1
	week_day <- 1
	while (N > 30){
		month <- month + 1
		if(month == 13) {
			year <- year + 1
			month <- 1
		}
		week_day <- week_day + 2
		N <- N - 30
	}
	print(paste0('Введённое число N', ' соответствует: ', N, ' ', months[month], ', ', week[(week_day + N - 2) %% 7 + 1], ', ', year, 'й год'))
	
}

{
	#Задание 2 (c учётом усложнения в классе)
	w <- c(0, 0, 0, 0, 0, 0, 0, 0)
	for (i in c(1:8)){
		a <- as.integer(readline('Введи число:'))
		w[i] <- a
	}
	w <- w[order(w, decreasing = TRUE)]
	for (i in c(1:7)){
		if (w[i] > w[i + 1]){
			 cat(w[i], ' > ', sep = '')
		}else{ 
			cat(w[i], ' = ', sep = '')
		}
	}
	cat(w[8], '\n')
}

{
	#Задание 3
	a <- 0
	while(toupper(a) != 'СТОП' | toupper(a) == 'STOP') {
		a <- readline('Введите переменную:' )
	} 
}

{
	#Задание 4
	N <- as.integer(readline('Введите N: '))
	sum <- 0
	for (i in c(1:N)){
		sum <- sum + i
	}
	print(sum)
}

{
	#Задание 5
	N <- as.character(readline("Введите N "))
	a = 0
	for (i in N){
		if (i >= '0' & i <= '9' | (i == '.' & a == 0)){
			if (i == '.') {
				a = 1
			}
			next
		}else {
			print('Это не число')
			a = 2
			break
		}
	}
	if (a < 2){
		print('Это число')
	}
}

{
	#Задание 6
	a <- as.integer(readline('Введите a: '))
	b <- as.integer(readline('Введите b: '))
	if (a > b){
		d <- a
		a <- b
		b <- d
	}
	b <- b - b %% 15
	while (a <= b){
		cat(b, '\n')
		b <- b - 15
	}
}


{
	#Задание 7
	N <- as.integer(readline('Введите число: '))

	months <- c('января', 'февраля', 'марта', 'апреля', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')
	dlit <- c(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	week <- c('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
	year <- 21
	month <- 1
	week_day <- 1
	while (N > dlit[month]){
		
		week_day <- (week_day + dlit[month]) %% 7 - 1) %% 7 + 1
		N <- N - dlit[month]
		month <- month + 1
		if(month == 13) {
			year <- year + 1
			month <- 1
		}
	}
	print(paste0('Введённое число N', ' соответствует: ', N, ' ', months[month], ', ', week[(week_day + N - 2) %% 7 + 1], ', ', year, 'й год'))
	
}	

{
	#Задание 11
	N <- as.integer(readline())
	for (i in (1:N)){
		#print(paste0(1:i, collapse = ""), quote = FALSE)
		cat(1:i, sep = '')
		cat('\n')
	}
}


