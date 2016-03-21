'use strict'

var PYTHON_SCRIPT_PATH = './files'

var http = require('http')
var child_process = require('child_process')
var fs = require('fs')


var handler = function(request, response){
  console.info('connection comes')
  response.end('ok')
}

var lookForwardFiles = function(path){
  return new Promise((res,rej)=>{
    fs.stat(path, (err, stat)=>{
      if(err) return res([])
      if(!stat.isDirectory()) return res([path])
      fs.readdir(path, (err, files)=>{
        if(err) return res([])
        var allP = files.map(f=>lookForwardFiles(path + '/' + f))
        Promise.all(allP).then(data=>res([].concat.apply([],data)))
      })
    })
  })
}

var fileListCache = []
var refreshFileListCache = function(){
  console.info('do refresh filelist')
  return lookForwardFiles(PYTHON_SCRIPT_PATH).then(data=>fileListCache=data)
}
refreshFileListCache()

var app = http.createServer(handler)
var io = require('socket.io')(app)
io.on('connection', socket => {
  var cp
  var startChildProcess = data => {
    var filePath = data.path
    if(cp) cp.kill()
    cp = child_process.spawn('python3', [filePath])
    cp.stdout.on('data', data => {
      socket.emit('data', data.toString())
    })
    cp.stderr.on('data', (data) => {
      socket.emit('cperr',data.toString())
    })
    cp.on('close', (code, b,c) => {
      socket.emit('close', `child process exited with code ${code}`)
    })
    socket.emit('newcp', filePath)
  }
  socket.emit('data','hi')
  socket.on('run', data => {
    startChildProcess(data)
  })
  socket.on('close', data=>{
    if(cp) cp.kill()
  })
  socket.on('command', data => {
    if(cp) {
      try {
        cp.stdin.write(data)
      } catch (e) {
        socket.emit('cperr', e.toString())
      } finally {
      }
    }
  })
  socket.on('refresh', data => {
    var sendCache = ()=>socket.emit('refresh', fileListCache)
    if(data && data.force){
      refreshFileListCache().then(sendCache)
    }else{
      sendCache()
    }
  })
})
app.listen(5466)
