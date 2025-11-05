function func1(){
    console.log('function 1 executed!!')
}

function func2(){
    console.log('function 2 executed!!')
}

function func3(){
   setTimeout(()=> console.log('function 3 executed!!'),3000)
}

function func4(){
    console.log('function 4 executed!!')
}

func1()
func2()
func3()
func4()





