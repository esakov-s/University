

source(file = 'C:\\Users\\Вячеслав\\Desktop\\Прога\\R\\interval_lib.R')

#Подопытные интервалы
a1 <- c(1, 5)
a2 <- c(1, 7, 9)
a3 <- c(2)
a4 <- c(-1, -3)
a5 <- c(-1, 1)


#Проверка работы функций

#1) is.interval

is.interval(a1)
is.interval(a2)
is.interval(a3)

#2) show.interval + as.interval

show.interval(a4)
show.interval(a2)

#3) plus.i

cat("Ожидаемый интервал: [0:6]\n")
cat("Рассчитанный интервал: ", sep = '')
show.interval(plus.i(a1, a5))

#4) minus.i

cat("Ожидаемый интервал: [-4:0]\n")
cat("Рассчитанный интервал: ", sep = '')
show.interval(minus.i(a4, a5))

#5) multi.i

cat("Ожидаемый интервал: [-5:5]\n")
cat("Рассчитанный интервал: ", sep = '')
show.interval(multi.i(a1, a5))

#6) div.i

cat("Ожидаемый интервал: [0,5:2,5]\n")
cat("Рассчитанный интервал: ", sep = '')
show.interval(div.i(a1, a3))


#Решение Примера 1
Cv <- as.interval(c(5, 6))
Q_prod <- as.interval(c(8, 12))
P <- as.interval(c(7, 10))
Q_sale <- as.interval(c(8, 12))

Pr1 <- multi.i(P, Q_sale)
Pr2 <- multi.i(Cv, Q_prod)
Pr <- minus.i(Pr1, Pr2) 
show.interval(Pr)
print("Значение ожидаемой прибыли получено")

R <- div.i(Pr, multi.i(Cv, Q_prod)) * 100
show.interval(R)
print("Значение рентабельности получено")