#= 
This is my implementation of Linear Regression in Julia =#

# How do I get to my conde?
# Is there a request package in Julia?
# Let's find out!

# using Pkg 
# Pkg.add("HTTP")
using VegaLite, DataFrames, Query
using HTTP

response = HTTP.request("GET", "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv")


r = String(response.body)

lines = split(r, "\n")


data = []


lines = lines[2:length(lines)]

lines[1]
splitted_line = split(lines[1], ",")
splitted_line[1]
typeof(Tuple(splitted_line))
typeof(splitted_line[1])

z = 1, 2
typeof(z)


for i in 1:length(lines)
    i = split(lines[i], ",")
    append!(data, Tuple(i))
end


data[1]