function func1(){
    console.log('Create Order!!')
}

function func2(){
    console.log('Make the payment!!')
}

function func3(cb){
   setTimeout(()=>{
     console.log('Deliver the order!!')
     cb()
    },3000)
}

function func4(){
         console.log('Eat!!')
}

func1()
func2()
func3(func4)


// *************************************************************************


// function func1(cb1,cb2,cb3){
//     console.log('Create Order!!')
//     cb1(cb2,cb3)
// }

// function func2(cb2,cb3){
//     console.log('Make the payment!!')
//     cb2(cb3)
// }

// function func3(cb){
//    setTimeout(()=>{
//      console.log('Deliver the order!!')
//      cb()
//     },3000)
// }

// function func4(){
//          console.log('Eat!!')
// }

// func1(func2,func3,func4)