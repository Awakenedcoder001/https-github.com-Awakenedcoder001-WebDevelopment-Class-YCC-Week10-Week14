// Data types:
// string,Number,Object,Array,Boolean,
// string
var name={"name":"Extended Family"}
console.log(name)

// number
var age={"age":30}
console.log(age)

//objects:
var details={"dsp":{
    "did":"DS(39)20-6986",
    "name":"Sonam Tobgay",
    "age":99,
    "gender":"Male"
}}
console.log(details)

var my_arr={"details":['Zangpo',"Web Development",99,"Ex-Monk"]}
console.log(my_arr)

var json_name=JSON.parse('{"name":"Extended Family"}')
console.log(json_name)

var json_age=JSON.parse('{"age":30}')
console.log(json_age)

var json_obj=JSON.parse(' {"dsp":{"name":"zangpo","course":"web development"}}')
console.log(json_obj)

var json_arr=JSON.parse('{"details":["Zangpo","Web Development",99,"Ex-Monk"]}')

console.log(json_arr)