'use strict'
var child_process = require('child_process')
var cp = child_process.spawn('python3', ['./files/circumference.py'])
cp.stdout.pipe(process.stdout)
process.stdin.pipe(cp.stdin)
cp.on('close', (code) => {
  process.exit(code)
})
