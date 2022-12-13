#2
{
	a1 <- as.integer(12)
	a2 <- 'aaa'
	a3 <- 1.2
	a4 <- 4 + 3i
	a5 <- TRUE
	print(paste(a1, typeof(a1)))
	print(paste(a2, typeof(a2)))
	print(paste(a3, typeof(a3)))
	print(paste(a4, typeof(a4)))
	print(paste(a5, typeof(a5)))
	print('', quote = FALSE)


	print(paste(29, typeof(29)), quote = FALSE)    # Все числа по умолчанию double
	print(paste(23i, typeof(23i)), quote = FALSE)  # Комплексное число
	print(paste(- 34L, typeof(-34L)), quote = FALSE) #Integer так как в конце числа double добавлен преобразователь в цело (L)
	print(paste(2 / 3, typeof(2 / 3)), quote = FALSE) # Не целочисленное деление -> результат double
	print(paste(4 / 2, typeof(4 / 2)), quote = FALSE) # (аналогично предыдущему выражению)
	print(paste(0xA, typeof(0xA)), quote = FALSE)	  #Число в шестнадцатиричной системе счисления (а числа по умолчанию double)
	print(paste(0xbL - 120L, typeof(0xbL - 120L)), quote = FALSE) # Целое - целое -> результат целый
	print(paste(0xbL - 120, typeof(0xbL - 120)), quote = FALSE) #Целое - дробное -> результат дробное
	print(paste(0xbL * 17, typeof(0xbL * 17)), quote = FALSE) #Целое * дробное -> результат дробный

}

#3
{
	a.ch <- readline()
	a.log <- as.logical(a.ch)
	a.int <- as.integer(a.ch)
	a.d <- as.double(a.ch)
	
	i_d <- a.int == a.d
	i_l <- a.int == a.log
	l_c <- a.log == a.ch
	d_l <- a.d == a.log
	d_c <- a.d == a.ch
	print(i_d)
	print(i_l)
	print(l_c)
	print(d_l)
	print(d_c)

}


{
	a <- 'z'
	b <- 'aaa'
	print(a < b)
}