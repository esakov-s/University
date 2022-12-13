
source(file = 'C:\\Users\\Вячеслав\\Desktop\\Прога\\R\\interval_lib.R')  # Путь под себя поменяй)

mean1 <- function(a, b){
  return((b + a) / 2.0)
}
Pr_count <- function(Cv, Q_prod, P, Q_sale){
  Pr1 <- multi.i(P, Q_sale)
  Pr2 <- multi.i(Cv, Q_prod)
  Pr <- minus.i(Pr1, Pr2)
  return(Pr)
}

R_count <- function(Cv, Q_prod, P, Q_sale){
  Pr <- Pr_count(Cv, Q_prod, P, Q_sale)
  R <- div.i(Pr, multi.i(Cv, Q_prod)) * 100
  return(R)
}


V_sales <- c()
Pr_diff <- c()

for (i in 0:1000){
  #=========Начальные интервалы
  Cv <- as.interval(c(5, 6))
  Q_prod <- as.interval(c(8, 12))
  P <- as.interval(c(7, 10))
  Q_sale <- as.interval(c(8, 8 + i * 0.5))
  
  
  
  #===========Работаем с прибылью
  Pr <- Pr_count(Cv, Q_prod, P, Q_sale)
  L0 <- Pr[2] - Pr[1]
  
  #Меняем Cv
  temp <- Cv
  Cv <- as.interval(mean1(Cv[1], Cv[2]))
  Pr_sh <- Pr_count(Cv, Q_prod, P, Q_sale)
  L1 <- L0 - (Pr_sh[2] - Pr_sh[1])
  Cv <- temp
  
  #Меняем Q_prod
  temp <- Q_prod
  Q_prod <- as.interval(mean1(Q_prod[1], Q_prod[2]))
  Pr_sh <- Pr_count(Cv, Q_prod, P, Q_sale)
  L2 <- L0 - (Pr_sh[2] - Pr_sh[1])
  Q_prod <- temp
  
  #Меняем P
  temp <- P
  P <- as.interval(mean1(P[1], P[2]))
  Pr_sh <- Pr_count(Cv, Q_prod, P, Q_sale)
  L3 <- L0 - (Pr_sh[2] - Pr_sh[1])
  P <- temp
  
  #Меняем Q_sale
  temp <- Q_sale
  Q_sale <- as.interval(mean1(Q_sale[1], Q_sale[2]))
  Pr_sh <- Pr_count(Cv, Q_prod, P, Q_sale)
  L4 <- L0 - (Pr_sh[2] - Pr_sh[1])
  Q_sale <- temp
  
  L_sum <- sum(L1, L2, L3, L4)
  
  L1 <- (L1 / L_sum) * 100
  L2 <- (L2 / L_sum) * 100
  L3 <- (L3 / L_sum) * 100
  L4 <- (L4 / L_sum) * 100
  
  L_sum_2 <- c(round(L1, 2), round(L2, 2), round(L3, 2), round(L4, 2))
  
  tbl1 <- data.frame('НУП' = c('C', 'Q_prod', 'P', 'Q_sale'), 'Ширина интервала неопр' = 0, 'Проц влияния неопр на результат' = 0)
  tbl1[1,2] <- max(Cv) - min(Cv)
  tbl1[2,2] <- max(Q_prod) - min(Q_prod)
  tbl1[3,2] <- max(P) - min(P)
  tbl1[4,2] <- max(Q_sale) - min(Q_sale)
  
  tbl1[1,3] <- L_sum_2[1]
  tbl1[2,3] <- L_sum_2[2]
  tbl1[3,3] <- L_sum_2[3]
  tbl1[4,3] <- L_sum_2[4]
  tbl1
  
  col1 <- c('yellow', 'green', 'blue', 'red', 'orange')
  fil1 <- c('yellow', 'green', 'blue', 'red', 'orange')
  pie(L_sum_2, labels = L_sum_2 , radius = 0.8, main = 'Процент уменьшения интервала прибыли \n решения по каждому \n управляющему параметру', col = col1)
  legend(-1.4, -0.45, c('C', 'Q_prod', 'P', 'Q_sale'), cex = 1.1, fill = fil1)
  
  V_sales <- c(V_sales, Q_sale[2] - Q_sale[1])
  Pr_diff <- c(Pr_diff, L4)
  print("Завершена работа с прибылью")
  
  
  
  #========================== Работаем с рентабельностью
  
  R <- R_count(Cv, Q_prod, P, Q_sale)
  
  L0 <- R[2] - R[1]
  
  #Меняем Cv
  temp <- Cv
  Cv <- as.interval(mean1(Cv[1], Cv[2]))
  R_sh <- R_count(Cv, Q_prod, P, Q_sale)
  L1 <- L0 - (R_sh[2] - R_sh[1])
  print(Cv)
  print(temp)
  Cv <- temp
  
  #Меняем Q_prod
  temp <- Q_prod
  Q_prod <- as.interval(mean1(Q_prod[1], Q_prod[2]))
  R_sh <- R_count(Cv, Q_prod, P, Q_sale)
  L2 <- L0 - (R_sh[2] - R_sh[1])
  Q_prod <- temp
  
  #Меняем P
  temp <- P
  P <- as.interval(mean1(P[1], P[2]))
  R_sh <- R_count(Cv, Q_prod, P, Q_sale)
  L3 <- L0 - (R_sh[2] - R_sh[1])
  P <- temp
  
  #Меняем Q_sale
  temp <- Q_sale
  Q_sale <- as.interval(mean1(Q_sale[1], Q_sale[2]))
  R_sh <- R_count(Cv, Q_prod, P, Q_sale)
  L4 <- L0 - (R_sh[2] - R_sh[1])
  Q_sale <- temp
  
  L_sum <- sum(L1, L2, L3, L4)
  
  L1 <- (L1 / L_sum) * 100
  L2 <- (L2 / L_sum) * 100
  L3 <- (L3 / L_sum) * 100
  L4 <- (L4 / L_sum) * 100
  
  L_sum_2 <- c(round(L1, 2), round(L2, 2), round(L3, 2), round(L4, 2))
  
  tbl2 <- data.frame('НУП' = c('C', 'Q_prod', 'P', 'Q_sale'), 'Ширина интервала неопр' = 0, 'Проц влияния неопр на результат' = 0)
  tbl2[1,2] <- max(Cv) - min(Cv)
  tbl2[2,2] <- max(Q_prod) - min(Q_prod)
  tbl2[3,2] <- max(P) - min(P)
  tbl2[4,2] <- max(Q_sale) - min(Q_sale)
  
  tbl2[1,3] <- L_sum_2[1]
  tbl2[2,3] <- L_sum_2[2]
  tbl2[3,3] <- L_sum_2[3]
  tbl2[4,3] <- L_sum_2[4]
  tbl2
  
  
  col1 <- c('yellow', 'green', 'blue', 'red', 'orange')
  fil1 <- c('yellow', 'green', 'blue', 'red', 'orange')
  pie(L_sum_2, labels = L_sum_2 , radius = 0.8, main = 'Процент уменьшения интервала рентабельности \n решения по каждому \n управляющему параметру', col = col1)
  legend(-1.4, -0.45, c('C', 'Q_prod', 'P', 'Q_sale'), cex = 1.1, fill = fil1)
  
  print("Работа с рентабельностью завершена")
}
print(V_sales)
print(Pr_diff)
plot(x = V_sales, y = Pr_diff, col = 'red', lwd = 4, type = "l")