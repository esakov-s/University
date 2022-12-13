getwd()
setwd('C:\\Users\\Вячеслав\\Desktop\\Учёба\\Эконометрика\\Семинар 2')
df <- read.table('2.txt', dec = ',', header = T)
df[1, ]


install.packages('lmtest')
library(lmtest)
