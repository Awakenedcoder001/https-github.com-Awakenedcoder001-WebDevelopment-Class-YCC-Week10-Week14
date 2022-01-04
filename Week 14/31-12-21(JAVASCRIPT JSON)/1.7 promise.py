var promise=new Promise((resolve, reject) =>{
    var x="Extended Family";
    var y="Extended Family";
    if(x===y){
        resolve("Strings are Equal")
    }
    else{
        reject("Strings are NOt equal")
    }
})

console.log(promise)