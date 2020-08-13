#= 
This is my implementation of Linear Regression in Julia =#

# How do I get to my conde?
# Is there a request package in Julia?
# Let's find out!

using Pkg 
# Pkg.add("HTTP")
Pkg.add("DataFrames")
using HTTP
using DataFrames




response = HTTP.request("GET", "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv")


r = String(response.body)

lines = split(r, "\n")


data = []


lines = lines[2:length(lines)]

lines[1]
split(lines[1], ",")
test = ["one, two", "three, four"]
typeof(test)
typeof(lines)
test[1]
lines[1]




splitted_line = split(lines[1], ",")
splitted_line
splitted_line[1]
typeof(Tuple(splitted_line))
typeof(splitted_line[1])

z = 1, 2
typeof(z)


for i in 1:length(lines)
    i = split(lines[i], ",")
    append!(data, i)
end

typeof(lines)
typeof(data)
typeof(data[1])

1 % 2







X = []
Y = []
for i in 1:length(data)
    if i % 2 == 1
        elem = parse(Float64, data[i])
        append!(X, elem)
    elseif i % 2 == 0
        elem = parse(Float64, data[i])
        append!(Y, elem)
    end
end

df = DataFrame(X=X, Y=Y)