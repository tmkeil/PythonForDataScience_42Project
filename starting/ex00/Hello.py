ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# A list is mutable (can be changed), so a value at index x can be changed
ft_list[1] = "World!"

# A tuple is immutable (cannot be changed), so we need to create a new one
ft_tuple = (ft_tuple[0], "Germany!")

# A set is mutable, but we cannot change an element directly,
# we need to remove it and add a new one
ft_set.remove("tutu!")
ft_set.remove("Hello")
ft_set.add("Hello")
ft_set.add("Heilbronn!")

# A dictionary is mutable
ft_dict["Hello"] = "42Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
