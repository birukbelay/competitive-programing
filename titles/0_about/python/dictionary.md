


## Find length of a dictionary
> len(dict)


##iterate over keys in dictionary
  
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

  ## delete value from a dictionary

```python
# delete an item from a dictionary
del a_dict[color]

```


## sort a dictionary
```python

d = {2:3, 1:89, 4:5, 3:0}
a=sorted(d.items())
print(a)
>> [(1, 89), (2, 3), (3, 0), (4, 5)] #this is a list
sd=dict(sorted(d.items()))
print(sd)
>> {1: 89, 2: 3, 3: 0, 4: 5} #this is a dictrionary
for k,v in sd:
     print( k, v)
```
> sorting by values
```python
a=dict(sorted(x.items(), key=lambda item: item[1]))
# Reversed
 a=dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
```
 