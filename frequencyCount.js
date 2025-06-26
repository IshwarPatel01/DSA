let str = "apple orange apple banana orange apple"

let freq = {}

let splitStr = str.split(" ")

for(let i = 0; i < splitStr.length; i++){
    freq[splitStr[i]] = (freq[splitStr[i]] || 0) + 1
    console.log(freq[splitStr[i]])
}

console.log(freq)