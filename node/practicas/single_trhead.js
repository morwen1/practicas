//single trheads


'use strict'

function single(){

    console.log('-------------------------------------------')
    console.log('           PROCESOS DE NODE                ')
    console.log('id del proceso.....................' + process.pid)
    console.log('titulo.............................' + process.title)
    console.log('directorio node....................' + process.execPath)



}

single()