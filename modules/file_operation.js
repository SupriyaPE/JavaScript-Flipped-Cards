const fs = require('fs')

let read_file = (file) => {
    fs.readFile(file,'utf8',(err,data)=>{
        if (err){
            console.err('Error reading file:',err)
            return;
        }
        console.log('File content:');
        console.log(data);
    });
}

let write_file = (file,contentToWrite) => {
    fs.writeFile(file,contentToWrite,(err)=>{
        if (err){
            console.err('Error writing file:',err)
            return;
        }
        console.log('content successfully written to file.');
    });
}

let append_file = (file,contentToAppend) => {
    fs.appendFile(file,contentToAppend,(err)=>{
        if (err){
            console.err('Error writing file:',err)
            return;
        }
        console.log('content successfully appended to file.');
    });
}


let delete_file = (file) => {
    fs.unlink(file,(err)=>{
        if (err){
            console.err('Error writing file:',err)
            return;
        }
        console.log('content successfully written to file.');
    });
}


let file_name1 = "one.txt"
let file_name2 = "two.txt"
let some_content = "\n\nGood Day!!"


// read_file(file_name1)
// write_file(file_name2, some_content)
// append_file(file_name2,some_content)
// delete_file(file_name2)




