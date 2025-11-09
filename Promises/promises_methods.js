let swiggy_order = new Promise((resolve,reject) => {

    setTimeout( ()=>{

            let async_func = true

                if(async_func){
                    resolve("Accepted order!!")
                }
                else{
                    reject("Out of stock")
                }
            },2000)
   }
);

swiggy_order.then((res) => console.log("Resolved:",res))
       .then(() => console.log("Your order will be reached shortly"))
       .catch((res) => console.log("Rejected:",res))
       .finally(()=> console.log("Transaction Completed!"))
    
    