trap <- function(p1, p2, p3, p4, up = 0, xl = 0, xr = 0, h = 0, d = 0){
  
  #============ Обработаем параметр up
  p2[2] <- p2[2] + up
  p3[2] <- p3[2] + up
  
  #============Смещение всей фигуры вверх вниз
  p1[2] <- p1[2] + h
  p2[2] <- p2[2] + h
  p3[2] <- p3[2] + h
  p4[2] <- p4[2] + h
  
  #============Смещение всей фигуры вправо влево
  p1[1] <- p1[1] + d
  p2[1] <- p2[1] + d
  p3[1] <- p3[1] + d
  p4[1] <- p4[1] + d
  
  #============Обработаем перемещение левой нижней точки вправо влево
  p1[1] <- p1[1] + xl
  
  #============Обработаем перемещение правой нижней точки вправо влево
  p4[1] <- p4[1] + xr
  
  #============ Определим x и рассчитаем y по x
  x <- p1[1]:p4[1]
  x <- seq(p1[1], p4[1])
  
  v <- c(p1[1], p2[1], p3[1], p4[1])
  x <- min(v):max(v)
  
  y <- 0
  
  #============ Уравнение прямой (x1, y1) и (x2, y2)
  # Y = Y1 + (Y2-Y1)/(X2-X1)*(x-x1)
  for (i in x) {
    j <- i - (p1[1] - 1)
    #========= Левая грань трапеции
    if (i <= p2[1]) {
      y[j] <- p1[2] + (p2[2] - p1[2])/(p2[1] - p1[1])*(i - p1[1])
    }
    #========= Верхнаяя грань
    if ((i > p2[1] & (i < p3[1]))) {
      y[j] <- p2[2]
    }
    #========= Правая грань
    if (i >= p3[1]) {
      y[j] <- p3[2] + (p4[2] - p3[2])/(p4[1] - p3[1])*(i - p3[1])
    }
  }
  
  plot(x = x, y = y, col = "red", lwd = 4, type = "l")
  
  
  #============Зададим значение y для основания трапеции
  
  y.bottom <- rep(p1[2], length(x))
  lines(x = x, y = y.bottom, col = "red", lwd = 4, type = "l")
}

#============ Зададим координаты точек
p1 <- c(100, 100)
p2 <- c(200, 200)
p3 <- c(400, 200)
p4 <- c(500, 100)

trap(p1, p2, p3, p4, 0, 0, 0, -3700, -5500)
