import json
from io import StringIO
# Encoding basic Python object hierarchies:

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

# output:["foo", {"bar": ["baz", null, 1.0, 2]}]

print(json.dumps('\u1234'))

# output: "\u1234"

print(json.dumps('\\'))

# output: "\\"

print(json.dumps({
  "A":0,
  "b":1,
  "c":2,
  "f":[
    "code","KashifNaqvi",
    "logic","code is art",
    "domain","do good have good"
  ],
  },sort_keys=True
))
# output: {"A": 0, "b": 1, "c": 2, "f": ["code", "KashifNaqvi", "logic", "code is art", "domain", "do good have good"]}
# ["streaming API", 1, 2, 3, 4, 5, 6]

io = StringIO()
json.dump(['streaming API',1,2,3,4,5,6],io)
print(io.getvalue())

# output: ["streaming API"]

# what  is Compact encoding: ?

a = json.dumps(([1,2,3,4,{1:2,3:4}]))
print("simple ",a)

b = json.dumps([1,2,3,4,{'4':5,"6":7}],separators=(',',':'))
print("with Compact encoding",b)


# Pretty printing:

print(json.dumps(
  {
    "name":"kashif",
    "program":"BS Computer Science",
    "level":"medium level developer",
    "understanding level":"normal",
    "understanding problem":"efficiently"
  }
  ,sort_keys=(True),indent=4))

# output:
#   {
#     "level": "medium level developer",
#     "name": "kashif",
#     "program": "BS Computer Science",
#     "understanding level": "normal",
#     "understanding problem": "efficiently"
#   }

# Decoding JSON:

print(json.loads('["foo",{"bar":["baz",null,1,2,3,4]}]'))

# output: ['foo', {'bar': ['baz', None, 1, 2, 3, 4]}]
print("----------------------------------------------------------------------------")

print(json.loads('"\\"foo\\bar"'))

# output: "foar

# Specializing JSON object decoding:


def as_complex(dict):
  if '__complex__' in dict:
    return complex(dict['real'],dict['imag' ])
  return dict

print(json.loads('{"__complex__":true,"real":1,"imag":2}',object_hook=as_complex))

# output: (1+2j)

def complex_work  (dict):
  if '__complex__' in (dict):
    return complex(dict["real"],dict["imag"])
  return dict
print(json.loads('{"__complex__":true,"real":13,"imag":56}',object_hook=complex_work))

# output:(13+56j)
print("----------------------------------WITH CLASS------------------------------------------")
# Extending JSONEncoder:

class ComplexEncoder(json.JSONEncoder):
  def default(self,obj):
    if isinstance(obj,complex):
      return [obj.real, obj.imag]
    return json.JSONEncoder.default(self,obj)
print(json.dumps(2+81j, cls=ComplexEncoder ))  

# output: [2.0, 81.0]

print(ComplexEncoder().encode(2+ 4j))

# output: [2.0, 4.0]

print(list(ComplexEncoder().iterencode(2+1j)))

# output:['[2.0', ', 1.0', ']']

# Using json.tool from the shell to validate and pretty-print:

