{
	# Задание 1
	w <- c(123, 4L, TRUE)
	typeof(w)
	mode(w)
	str(w)
	#mode представляет более общую информацию о типе элементов векторов(вместо double numeric)
	# во отличие от typeof
	# str выводит полную инфрмацию о векторе : типа данных, диапазон нумерации ячеек и их значения	
}

{
	# Задание 2
	w1 <- c(-12L, 4, 'Level 2', 8.2, TRUE)
	w2 <- c(0, 56 / 6, FALSE, FALSE, 18)
	w3 <- c(Inf, NULL, NA, FALSE, 18, NaN)
	w4 <- c(Inf, NULL, NA, FALSE, 18L, NaN)
	w5 <- c(Inf, NULL, NA, FALSE, '18', NaN)
	w6 <- c(NULL)
	typeof(w1)
	length(w1)
	typeof(w2)
	length(w2)
	typeof(w3)
	length(w3)
	typeof(w4)
	length(w4)
	typeof(w5)
	length(w5)
	typeof(w6)
	length(w6)
	# Длины всех векторов кроме последнего - 5, последний размера 0
	# вектора w3 и w4 имеют одинаковый тип(double), так как оба имеют в составе элемент Inf, имеющий тип double
}

{
	# Задание 3
	w1 <- rep(c(0, -1, 1:3), times = 3)
	w2 <- rep(c(0, -1, 1:3), each = 3)
	w3 <- rep(c(0, -1, 1:3), each = 3, times = 2)
	#Параметр times повторяет вектор некоторое число раз, параметр each повторяет каждый элемент указанное число раз
	#each выполняется раньше time
}

{
	# Задание 4
	
}
