

- iterate over keys in dictionary
  
```python

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# prints keys of the dictionary
>>> for key in a_dict:
...     print(key)
...
color
fruit
pet
>>> for item in a_dict.items():
     print(item)
# ...returns 
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')

# getting key value pairs
>>> for key, value in a_dict.items():
...     print(key, '->', value)


# gettins only the keys as array
>>> keys = a_dict.keys()
>>> keys= dict_keys(['color', 'fruit', 'pet'])

>>> for value in a_dict.values():
...     print(value)
# ...printing values
blue
apple
dog



```

- delete value from a dictionary

```python
# delete an item from a dictionary
del a_dict[color]

```
