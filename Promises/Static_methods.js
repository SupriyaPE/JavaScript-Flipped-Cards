let p1 = Promise.resolve("food ordered")

let p2 = new Promise((res,rej) => {
            // res("order received")
            rej("out of stock")
})

let p3 = new Promise((res,rej) => {
    setTimeout(() => { res("order not delivered")},2000)})

    // Promise.all([p1,p2,p3])
    // .then((results) => console.log(results))
    // .catch((message) => console.log(message))
    

    //  Promise.race([p2,p1,p3])
    // .then((results) => console.log(results))
    // .catch((message) => console.log(message))
    

    //  Promise.allSettled([p1,p2,p3])
    // .then((results) => console.log(results))
    // .catch((message) => console.log(message))
    

     Promise.any([p2,p1,p3])
    .then((results) => console.log(results))
    .catch((message) => console.log(message))
    