#= 
This is my implementation of Linear Regression in Julia =#

# How do I get to my conde?
# Is there a request package in Julia?
# Let's find out!

using Pkg 
# Pkg.add("HTTP")
# Pkg.add("DataFrames")
using HTTP
using DataFrames
using LinearAlgebra



response = HTTP.request("GET", "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv")

r = String(response.body)

lines = split(r, "\n")
data = []

for i in 1:length(lines)
    i = split(lines[i], ",")
    append!(data, i)
end

data = data[3:length(data) - 1]

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

# df = DataFrame(X=X, Y=Y)

on1s = ones(1, length(df.X))
X = convert(Array{Float64}, X)
features = [transpose(on1s) X]
outcome = convert(Array{Float64}, Y)

# Calculate the regression parameters
# OLS formula: beta_hat = ((X'X)^-1)X'Y

x_prime_x = transpose(features) * features
xx_to_minusone = inv(x_prime_x)
x_prime_y = transpose(features) * Y
beta_hat = xx_to_minusone * x_prime_y


