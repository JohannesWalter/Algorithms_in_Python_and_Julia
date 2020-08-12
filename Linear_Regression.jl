#= 
This is my implementation of Linear Regression in Julia =#

# How do I get to my conde?
# Is there a request package in Julia?
# Let's find out!

# using Pkg 
# Pkg.add("HTTP")

using HTTP

response = HTTP.request("GET", "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv")

println(response.status)
println(String(response.body))
typeof(response.body)
typeof(String(response.body))
r = String(response.body)
lines = split(r, "\n")

data = []

for item in lines
    split(item, ",")
    append!(data, item)
end

print("Everything went well")
typeof(data)

